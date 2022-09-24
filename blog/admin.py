from atexit import register
from django.contrib import admin

from .models import BlogPost, BlogComment

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_modified', 'is_active')
    list_display_links = ('title',)
    list_editable = ('is_active',)


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'datetime_created', 'is_active')
    list_display_links = ('author',)
    list_editable = ('is_active',)
    list_filter = ('post', 'author', 'is_active')
