from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextField()
    blog_image = models.ImageField(upload_to='blog/', blank=True)
    is_active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
