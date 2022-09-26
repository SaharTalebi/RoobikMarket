from django.contrib import admin

from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'datetime_modified')
    list_display_links = ('title',)
    list_editable = ('is_active',)


