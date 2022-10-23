from django import forms

from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ('person', 'first_name', 'last_name', 'phone_number', 'p_id', 'cart_number',)