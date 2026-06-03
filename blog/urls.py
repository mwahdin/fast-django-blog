from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, AuthorView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('author', AuthorView.as_view(), name='author_page'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]

