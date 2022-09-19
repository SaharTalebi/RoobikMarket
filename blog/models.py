from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextField()
    blog_image = models.ImageField(upload_to='blog/', blank=True)
    is_active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_post_detail", kwargs={"pk": self.pk})
    

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, verbose_name='Post Name', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), verbose_name='Post Author', on_delete=models.CASCADE, related_name='comments')
    comment_body = RichTextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

