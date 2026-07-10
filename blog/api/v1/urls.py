# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewsett

app_name = 'api-v1'

router = DefaultRouter()
router.register(r'posts', PostViewsett, basename='post')

urlpatterns = [
    #modelViewSet
    path('', include(router.urls)),


    #ViewSet
    path('post/',PostViewsett.as_view({'get': 'list', 'post': 'create'}), name="post-list" ),
    path('post/<int:pk>/',PostViewsett.as_view({'get': 'retrieve'}), name="post-list" ),
]