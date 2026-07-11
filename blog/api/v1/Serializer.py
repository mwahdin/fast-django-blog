from rest_framework import serializers
from ...models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'status',
            'title',
            'slug',
            'content',
            'snippet',
            'publish_date',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= [
            'id',
            'name',
            'content',
            'image',
            'slug',
        ]