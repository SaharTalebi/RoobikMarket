from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from accounts.models import CustomUser

# Create your models here.

class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories" 

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])


class FeaturedProductCategory(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "featured products categories" 

    def __str__(self):
        return self.name


class Product(models.Model):
    WARRANTY_CHOICES = (
        ('0', 'بدون گارانتی'),
        ('6', 'گارانتی 6 ماهه'),
        ('12', 'گارانتی 12 ماهه'),
    )

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    featured_category = models.ManyToManyField(FeaturedProductCategory, related_name='products', blank=True)
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
    is_special_sale = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # Manager
    objects = models.Manager()
    active_product = ActiveProductManager()

    class Meta:
        ordering = ('-datetime_created',)

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

    class Meta:
        ordering = ('-datetime_created',)

    