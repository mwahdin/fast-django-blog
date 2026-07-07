from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .Serializer import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404


class PostList(APIView):
    """
    Retrieve a list of published posts and create new post
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """retrieving a list of posts"""
        posts = Post.objects.filter(status=Post.Status.PUBLISHED)
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """create a post with provided data"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetail(APIView):
    """
    getting detail of the post and edit plus remove it
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


    def get(self, request, id):
        """retrieving the post data"""
        post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        """editing the post data"""
        post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        """deleting post data"""
        post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
        post.delete()
        return Response({"details":"the target post was deleted!"},  status=status.HTTP_204_NO_CONTENT)

