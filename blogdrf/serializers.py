from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CategoryModel, BlogPostModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'title']


class BlogPostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    # category = CategorySerializer(many=True)
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=CategoryModel.objects.all(), many=True
    # )

    class Meta:
        model = BlogPostModel
        fields = ["id", "title", "content", "category", "tags", "created_at", "updated_at"]
