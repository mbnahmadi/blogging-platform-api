from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import BlogPostModel, CategoryModel
from .serializers import BlogPostSerializer, CategorySerializer

from drf_yasg. utils import swagger_auto_schema


class CreateBlogPostView(generics.CreateAPIView):
    '''
    create post
    '''
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer


class UpdateBlogPostView(generics.UpdateAPIView):
    '''
    update post (support Patch/Put and Get)
    '''    
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer


class DeleteBlogPost(generics.DestroyAPIView):
    '''
    Delete post (support Delete and Get)
    '''
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer


class RetrieveBlogPost(generics.RetrieveAPIView):
    '''
    show special post (Get and show just one post)
    '''
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer


class GetAllBlogPost(generics.ListAPIView):
    '''
    show all posts (Get)/and add filter field 
    '''  
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer
    filterset_fields = ["category"]  
    ordering_fields = ["id"]
    search_fields = ["title", "content", "tags", "category__title"]
    # def get_queryset(self):
    #     '''
    #     return filtered querysets with category 
    #     '''
    #     queryset = BlogPostModel.objects.all()
    #     category = self.request.query_params.get('category')
    #     if category is not None:
    #         queryset = queryset.filter(category=category)
    #     return queryset    
        