from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .Serializer import PostSerializer
from ...models import Post


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)