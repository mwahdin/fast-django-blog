from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, User, Category, Tag
from django.db.models import Count, Q


class TopAuthorsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["top_authors"] = (
            User.objects.annotate(
                published_post_count=Count(
                    "blog_posts", filter=Q(blog_posts__status=Post.Status.PUBLISHED)
                )
            )
            .filter(published_post_count__gt=0)
            .order_by("-published_post_count")[:5]
        )

        return context


class PopularTagsMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popular_tags"] = Tag.objects.annotate(
            posts_count=Count("posts")
        ).order_by("-posts_count")[:6]

        return context


class AuthorView(ListView):
    model = Post
    template_name = "blog/author.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.kwargs["username"])
        return Post.objects.filter(
            author=self.author, status=Post.Status.PUBLISHED
        ).order_by("-publish_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.author
        return context


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).order_by(
            "-publish_date"
        )


# class PostDetailView(PopularTagsMixin, DetailView):
#     model = Post
#     template_name = "blog/single.html"
#     context_object_name = "post"

#     def get_object(self, queryset=None):
#         safe_queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
#         obj = super().get_object(queryset=safe_queryset)
#         viewed_posts = self.request.session.get("viewed_posts", [])
#         if obj.id not in viewed_posts:
#             obj.views_count += 1
#             obj.save(update_fields=["views_count"])
#             viewed_posts.append(obj.id)
#             self.request.session["viewed_posts"] = viewed_posts
#             self.request.session.modified = True
#         return obj

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         current_post = self.object
#         context["related_posts"] = (
#             Post.objects.filter(
#                 status=Post.Status.PUBLISHED, category__in=current_post.category.all()
#             )
#             .exclude(id=current_post.id)
#             .distinct()[:4]
#         )
#         return context

class PostDetailView(PopularTagsMixin, DetailView):
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    template_name = "blog/single.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)         
        viewed_posts = self.request.session.get("viewed_posts", [])
        if obj.id not in viewed_posts:
            obj.views_count += 1
            obj.save(update_fields=["views_count"])
            viewed_posts.append(obj.id)
            self.request.session["viewed_posts"] = viewed_posts
            self.request.session.modified = True
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.object
        
        context["related_posts"] = (
            Post.objects.filter(
                status=Post.Status.PUBLISHED, category__in=current_post.category.all()
            )
            .exclude(id=current_post.id)
            .distinct()[:4]
        )
        return context


class AllCategoriesListView(ListView):
    model = Category
    template_name = "blog/category.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.annotate(
            approved_posts_count=Count(
                "posts", filter=Q(posts__status=Post.Status.PUBLISHED)
            )
        ).order_by("name")


class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/category.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return Post.objects.filter(
            category=self.category, status=Post.Status.PUBLISHED
        ).order_by("-publish_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context
    

class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['status', 'image', 'title', 'slug', 'content', 'snippet', 'category', 'tags']
    success_url = reverse_lazy('blog:post_list')
    permission_required = 'blog.add_post'
    raise_exception = True

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['status', 'image' ,'title', 'content', 'snippet', 'category', 'tags']
    template_name = 'blog/edit_post.html'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug})

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj