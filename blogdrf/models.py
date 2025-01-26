from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=250)
    status = models.BooleanField()
    position = models.IntegerField()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['position']

    def __str__(self):
        return f"{self.title}"


class BlogPostModel(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ManyToManyField(CategoryModel)
    tags = ArrayField(models.CharField(max_length=50))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ("id",)

    def __str__(self):
        return f"{self.pk}"    



