from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post

# Create your views here.
class AuthorView(TemplateView):
    template_name = 'blog/author.html'


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
    context_objeect_name = 'post'

class PostCreateView(CreateView):
    pass