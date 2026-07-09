# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

app_name = 'api-v1'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]