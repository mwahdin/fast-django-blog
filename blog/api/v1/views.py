
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .Serializer import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404


@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=Post.Status.PUBLISHED)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
    if request.method =="GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method =="PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method =="DELETE":
        post.delete()
        return Response({"details":"the target post was deleted!"})














# @api_view(["GET", "PUT","DELETE"])
# def postDetaill(request, id):
#     post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)

#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True) 
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"the target post was deleted"}, status=204)



# @api_view(["GET", "POST"])
# def postListt(request):
#     if request.method == "GET":
#         post = Post.objects.filter(status=Post.Status.PUBLISHED)
#         serializer = PostSerializer(post, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
    