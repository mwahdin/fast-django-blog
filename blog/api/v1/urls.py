from django.urls import path
from .views import postList, postDetail

app_name='api-v1'

urlpatterns = [
    path('posts/',postList, name='posts_list'),
    path('posts/<int:id>/',postDetail, name='posts_Detaile'),
]
 