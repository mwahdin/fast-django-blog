from django.urls import path
from .views import (PostListView, PostDetailView, AuthorView, AllCategoriesListView, CategoryPostListView, CreatePostView, PostUpdateView, PostDeleteView, SearchResultsView)

app_name = 'blog' 

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/create/', CreatePostView.as_view(), name='post_create'),
    path('<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('categories/', AllCategoriesListView.as_view(), name='all_categories'),
    path('category/<slug:slug>/', CategoryPostListView.as_view(), name='category_posts'),
    path('author/<str:username>/', AuthorView.as_view(), name='author_page'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchResultsView.as_view(), name='post_search'),
]