from rest_framework import serializers

from blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id','title','description','blog_image','is_active','datetime_created','datetime_modified',)