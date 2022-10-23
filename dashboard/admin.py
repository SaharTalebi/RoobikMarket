from atexit import register
from django.contrib import admin

from .models import PersonalInfo
# Register your models here.

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('person', 'phone_number', 'first_name', 'last_name',)

