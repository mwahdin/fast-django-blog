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
        return Post.objects.filter(status=Post.Status.PUBLISHED).select_related('author').prefetch_related('category', 'tags').order_by(
            "-publish_date"
        )

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


class SearchResultsView(ListView):
    model=Post
    template_name="website/search-results.html"
    context_object_name = "posts"
    paginate_by = 10
    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            return Post.objects.filter(status=Post.Status.PUBLISHED).select_related('author').prefetch_related('category', 'tags').filter(
                Q(title__icontains=query) | 
                Q(snippet__icontains=query) | 
                Q(content__icontains=query)
            ).order_by("-publish_date")
            
        return Post.objects.none()



# ==============================================================================
# 🏋️‍♂️ PRACTICE VIEWS (QuerySet Optimization & Overriding Methods Practice)
# ==============================================================================

class UserPosts(LoginRequiredMixin ,ListView):
    
    model = Post
    template_name = "blog/category.html"
    context_object_name = 'my_posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).prefetch_related('tags')
    
class MustViewPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/category.html"
    context_object_name = 'top_five_posts'

    def get_queryset(self):
        return Post.objects.filter(status= Post.Status.PUBLISHED).prefetch_related('category').select_related('author').order_by('-views_count')[:5]
    

class AllTagListView(ListView):
    model = Tag
    template_name = "blog/category.html"
    context_object_name = 'all_tags'

    def get_queryset(self):
        return Tag.objects.annotate(published_posts_count=Count('posts', filter=Q(posts__status=Post.Status.PUBLISHED))).order_by('-published_posts_count')

class AdvanseSearch(ListView):
    model=Post
    template_name="website/search-results.html"
    context_object_name= 'filtered_posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        cat_id = self.request.GET.get('category_id')
        min_views = self.request.GET.get('min_views')
        queryset = Post.objects.filter(status= Post.Status.PUBLISHED).prefetch_related('category').select_related('author')

        if query:
            queryset = queryset.filter(Q(title__icontains=query)| Q(content__icontains=query))
        
        if cat_id:
            queryset = queryset.filter(category__id=cat_id)


        if min_views:
            queryset = queryset.filter(views_count__gte=min_views)

        return queryset

class HotTagsListView(ListView):
    model = Tag
    template_name = "blog/hot_tags.html"
    context_object_name = "tags"

    def get_queryset(self):
        return Tag.objects.annotate(hot_tags=Count('posts', filter=Q(posts__status=Post.Status.PUBLISHED))).order_by('-hot_tags')[:5]
    


import datetime
from django.utils import timezone
    
class TrendingThisWeekListView(ListView):
    model = Post
    template_name = "blog/trending.html"
    context_object_name = "posts"

    def get_queryset(self):
        time_threshold = timezone.now() - datetime.timedelta(days=7)
        
        queryset = Post.objects.filter(status=Post.Status.PUBLISHED).select_related('author').prefetch_related('category', 'tags')
        queryset = queryset.filter(publish_date__gte=time_threshold).order_by('-views_count')
        return queryset
class HomeBlogView(ListView):
    model=Post
    template_name="blog/home.html"
    context_object_name='posts'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categorys"] = Category.objects.all()
        return context

from django.http import Http404
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_object(self, queryset=None):
       
        obj = super().get_object(queryset=None)
        
        if obj.status == Post.Status.DRAFT and obj.author != self.request.user:
            raise Http404("این مقاله هنوز منتشر نشده است.")
        
        else:
            return obj
        
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'snippet', 'category']  
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'snippet', 'category']
    template_name = "blog/post_form.html"

    def get_success_url(self):
        post_slug = self.object.slug
        
        return reverse('blog:post_detail', kwargs={'slug': post_slug})
        