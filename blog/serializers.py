from rest_framework import serializers
from .models import PostsModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsModel
        fields = '__all__'
