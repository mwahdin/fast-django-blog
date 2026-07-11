# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet, CategoryModelViewSet

app_name = 'api-v1'
router = DefaultRouter()
router.register('posts', PostModelViewSet, basename="posts")
router.register('category', CategoryModelViewSet, basename="posts-category")
urlpatterns = router.urls

