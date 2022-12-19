from rest_framework import serializers

from blog.models import BlogPost
from accounts.models import CustomUser


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id','title','description','blog_image','is_active','datetime_created','datetime_modified',)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"