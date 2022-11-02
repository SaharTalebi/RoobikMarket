from atexit import register
from django.contrib import admin

from .models import CustomUser
from dashboard.models import Address

# Register your models here.

class AddressesInline(admin.TabularInline):
    model = Address
    fields = ['state', 'city', 'postal_code', 'full_address', 'phone_no', 'delivery_person']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')
    inlines = [AddressesInline,]

