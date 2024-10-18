# from db_connection import db
# posts_collection = db['posts']
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class PostsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50)
    tags = ArrayField(models.CharField(max_length=100))
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)