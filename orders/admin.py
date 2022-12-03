from django.contrib import admin

from .models import Orders, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'product', 'quantity', 'price')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    model = Orders
    list_display = ('f_name', 'l_name', 'phone_no', 'created_date', 'is_paid',)
    inlines = (OrderItemInline, )
    

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('order', 'product', 'quantity', 'price', )
