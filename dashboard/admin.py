from django.contrib import admin

from .models import Address

@admin.register(Address)
class AddressesAdmin(admin.ModelAdmin):
    model = Address
    list_display = ('person', 'state', 'city', 'full_address', 'postal_code', 'phone_no', 'delivery_person', 'is_selected')
    list_filter = ('person', 'state', 'city')