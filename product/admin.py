from django.contrib import admin

from .models import Product, ProductComment, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'datetime_modified')
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_filter = ('category', 'is_active')

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'is_active', 'datetime_created')
    list_display_links = ('author', 'product')
    list_editable = ('is_active',)
    list_filter = ('author', 'product', 'is_active',)

admin.site.register(Category)


