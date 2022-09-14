from atexit import register
from django.contrib import admin

from .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_modified', 'is_active')
    list_display_links = ('title',)
