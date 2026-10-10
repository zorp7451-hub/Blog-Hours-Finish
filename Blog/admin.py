from django.contrib import admin
from .models import Blogs, Category, Comment, Tags

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'category', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] if hasattr(Category, 'title') else ['id', 'name']
    search_fields = ['title'] if hasattr(Category, 'title') else ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'user', 'parent', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] if hasattr(Tags, 'title') else ['id', 'name']
    search_fields = ['title'] if hasattr(Tags, 'title') else ['name']