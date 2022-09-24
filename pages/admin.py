from django.contrib import admin

from .models import ContactUs

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'datetime_created')
    list_filter = ('name', 'datetime_created',)
    list_display_links = ('name', 'email',)

admin.site.register(ContactUs, ContactUsAdmin)
