from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post, User, Category


#return render(request, 'blog/author_page.html', context)
class AuthorView(TemplateView):
    model = Post
    template_name = 'blog/author.html'
    context_object_name = 'posts'

    def get_queryset(self):
        
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=self.author, status=Post.Status.PUBLISHED).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['author'] = self.author
        return context
        

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish_date')
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_object(self, queryset = None):
        safe_queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
        obj = super().get_object(queryset=safe_queryset)
        viewed_posts = self.request.session.get('viewed_posts', [])
        if obj.id not in viewed_posts:
            obj.counted_views += 1
            obj.save(update_fields=['counted_views'])
            viewed_posts.append(obj.id)
            self.request.session['viewed_posts'] = viewed_posts
            self.request.session.modified = True
        return obj
        

class AllCategoriesListView(ListView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'category'

    def get_queryset(self):
        return Category.objects.annotate(approved_posts_count = Count('posts', filter=Q(posts__status=Post.Status.PUBLISHED))).order_by('name')



    


    
class CategoryPostListView(ListView):
    model = Post                        
    template_name = 'blog/category.html' 
    context_object_name = 'posts'       

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(categories=self.category, status=Post.Status.PUBLISHED).order_by('-publish_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category 
        return context