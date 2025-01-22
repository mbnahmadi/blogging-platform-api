from rest_framework import serializers

from .models import CategoryModel, BlogPostModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title']


class BlogPostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    # category = CategorySerializer(many=True)
    class Meta:
        model = BlogPostModel
        fields = ["title", "content", "category", "tags", "created_at", "updated_at"]