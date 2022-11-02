from dataclasses import fields
from django import forms

from .models import Address
from accounts.models import CustomUser


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('state', 'city', 'full_address', 'postal_code', 'phone_no', 'delivery_person')

