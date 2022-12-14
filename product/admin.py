from django.contrib import admin

from .models import Product, ProductComment, Category, FeaturedProductCategory


class CommentsInline(admin.TabularInline):
    model = ProductComment
    fields = ['author', 'comment_body', 'is_active']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_special_sale', 'is_active',)
    list_display_links = ('title',)
    list_editable = ('is_active', 'is_special_sale', 'category')
    list_filter = ('category', 'featured_category', 'is_active', 'is_special_sale')
    inlines = [CommentsInline,]

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'is_active', 'datetime_created')
    list_display_links = ('author', 'product')
    list_editable = ('is_active',)
    list_filter = ('author', 'product', 'is_active',)

class CategoryAdmin(admin.ModelAdmin):
    cate_name = Category.objects.filter(parent=None)
    list_filter = ('name',)
admin.site.register(Category, CategoryAdmin)

admin.site.register(FeaturedProductCategory)


