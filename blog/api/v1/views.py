from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets 
from rest_framework.response import Response 
from .Serializer import PostSerializer
from ...models import Post
from ...models import Post, Category


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()