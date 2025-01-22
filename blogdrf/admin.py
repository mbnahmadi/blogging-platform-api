from django.contrib import admin
from .models import CategoryModel, BlogPostModel

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    search_fields = ('title',)

admin.site.register(CategoryModel, CategoryAdmin)



class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_category', 'tags', 'created_at']
    list_filter = ['category', 'tags']
    search_fields = ['title', 'get_category', 'tags']

    def get_category(self, obj):
        return ", ".join([cat.title for cat in obj.category.all()]) 
    get_category.short_description = 'category'



admin.site.register(BlogPostModel, BlogPostAdmin)    