from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post, User


# Create your views here.
def author_posts(request, username):
    author = get_object_or_404(User, username=username)
    
    posts = Post.objects.filter(author=author, status='published').order_by('-created_at')
    
    context = {
        'author': author,
        'posts': posts,
    }
    
    return render(request, 'blog/author_page.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-published_date')
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    pass