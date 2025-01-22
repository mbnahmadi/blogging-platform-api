from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import BlogPostModel, CategoryModel
from .serializers import BlogPostSerializer, CategorySerializer

from drf_yasg. utils import swagger_auto_schema

# Create your views here.

class CreateBlogPostView(generics.CreateAPIView):
    '''
    create post
    '''
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer


class UpdateBlogPostView(generics.UpdateAPIView):
    '''
    update post
    '''    

