from django.shortcuts import render
from .serializers import PostSerializer
from .models import PostsModel
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from django.db.models import Q
# Create your views here.


class Create_post(APIView):
    @swagger_auto_schema(request_body=PostSerializer)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'post created successfuly!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Get_all_posts(APIView):

    def get(self,request):
        posts = PostsModel.objects.all()
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)
    

class Get_post(APIView):

    def get(self,request,pk):
        try:
            posts = PostsModel.objects.get(pk=pk)
            serializer = PostSerializer(posts)  
            return Response(serializer.data)
        except PostsModel.DoesNotExist:
            return Response({'error':'Post not found'},status=status.HTTP_404_NOT_FOUND)
        

class Delete_post(APIView):
    def delete(self,request,pk):
        try:
            posts =  PostsModel.objects.get(pk=pk)
            posts.delete()
            return Response({'message':'The post with id {pk} deleted!'},status=status.HTTP_204_NO_CONTENT)
        except PostsModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class Update_post(APIView):
    @swagger_auto_schema(request_body=PostSerializer)
    def put(self,request,pk):
        try:
            posts = PostsModel.objects.get(pk=pk)
        except PostsModel.DoesNotExist:
            return Response({'error':'post not found'},status=status.HTTP_404_NOT_FOUND)    
        serializer = PostSerializer(data=request.data , instance=posts)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'post update successfuly'} ,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    

class SearchView(APIView):
    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('term', openapi.IN_QUERY, description="Search term for title, content, and category", type=openapi.TYPE_STRING)]
        )
    
    def get(self,requset):
        term = requset.query_params.get('term')

        if term:
            posts = PostsModel.objects.filter(
                Q(title__icontains=term)|
                Q(content__icontains=term)|
                Q(category__icontains=term)
            )
        else:
            return Response({'error':'term is required.'},status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)        





