from django import forms

class AddToCartForm(forms.Form):
    QUANTTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
    
    quantity = forms.TypedChoiceField(choices=QUANTTITY_CHOICES, coerce=int)