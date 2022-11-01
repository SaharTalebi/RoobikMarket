from django import forms

from accounts.models import CustomUser


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

