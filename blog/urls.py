"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Create_post,Get_all_posts,Get_post,Delete_post,Update_post,SearchView

urlpatterns = [
    path('create-post/' , Create_post.as_view(), name="create-post"),
    path('get-all-posts/' , Get_all_posts.as_view(), name="get-all-post"),
    path('get-post/<str:pk>/' , Get_post.as_view(), name="get-post"),
    path('delete-post/<str:pk>/' , Delete_post.as_view(), name="delete-post"),
    path('update-post/<str:pk>/' , Update_post.as_view(), name="update-post"),
    path('search/' , SearchView.as_view(), name="search"),

]
