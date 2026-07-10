from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets 
from rest_framework.response import Response 
from .Serializer import PostSerializer
from ...models import Post

#modelViewSet
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)

#ViewSet
class PostViewsett(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)
    
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request, pk=None):
        postObject = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(postObject)
        return Response(serializer.data)

    def create(self, request):
        pass