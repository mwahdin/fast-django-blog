from django.urls import path
from .views import (PostListView, PostDetailView, AuthorView, AllCategoriesListView, CategoryPostListView)

app_name = 'blog' 

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('categories/', AllCategoriesListView.as_view(), name='all_categories'),
    path('category/<slug:slug>/', CategoryPostListView.as_view(), name='category_posts'),
    path('author/<str:username>/', AuthorView.as_view(), name='author_page'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]