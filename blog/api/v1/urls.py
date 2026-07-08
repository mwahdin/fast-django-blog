from django.urls import path
from .views import PostDetail, PostList

app_name='api-v1'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-lists'),
    path("posts/<int:pk>", PostDetail.as_view(), name='post-detail'),
]
 