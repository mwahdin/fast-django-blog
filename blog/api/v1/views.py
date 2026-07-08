
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from .Serializer import PostSerializer
from ...models import Post


# class PostList(APIView):
#     """
#     Retrieve a list of published posts and create new post
#     """
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request):
#         """retrieving a list of posts"""
#         posts = Post.objects.filter(status=Post.Status.PUBLISHED)
#         serializer = self.serializer_class(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         """create a post with provided data"""
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    
class PostList(
    GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(
    GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)

    def get(self, request, *args, **kwargs):
        """retrieving the post data"""
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        """retrieving the post data"""
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# class PostDetail(APIView):
#     """
#     getting detail of the post and edit plus remove it
#     """
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer


#     def get(self, request, id):
#         """retrieving the post data"""
#         post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         """editing the post data"""
#         post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         """deleting post data"""
#         post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
#         post.delete()
#         return Response({"details":"the target post was deleted!"},  status=status.HTTP_204_NO_CONTENT)

