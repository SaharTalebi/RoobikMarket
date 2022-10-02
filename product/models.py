from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from accounts.models import CustomUser

# Create your models here.

class Product(models.Model):
    WARRANTY_CHOICES = (
        ('0', 'بدون گارانتی'),
        ('6', 'گارانتی 6 ماهه'),
        ('12', 'گارانتی 12 ماهه'),
    )

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    description = RichTextField()
    product_image = models.ImageField(upload_to='product/')
    product_image1 = models.ImageField(upload_to='product/', null=True, blank=True)
    product_image2 = models.ImageField(upload_to='product/', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='product/', null=True, blank=True)
    price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    warranty = models.CharField(max_length=50, choices=WARRANTY_CHOICES)
    is_active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    

class ProductComment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='product_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment_body = RichTextField()
    is_active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    