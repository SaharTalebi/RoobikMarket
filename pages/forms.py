from django import forms

from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'phone', 'email', 'subject', 'text')

    name= forms.CharField(
        label= 'نام شما :',
        required= False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'dir': 'rtl',
            })
    )

    phone= forms.CharField(
        label= 'تلفن تماس :',
        required= False,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'dir': 'rtl',
            }
        )
    )

    email= forms.EmailField(
        label= 'پست الکترونیک :',
        widget= forms.EmailInput(
            attrs= {
                'class': 'form-control',
                'dir': 'rtl',
            }
        )
    )

    subject= forms.CharField(
        label= 'موضوع پیام :',
        required= False,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'dir': 'rtl',
            }
        )
    )

    text= forms.CharField(
        label= 'متن پیام :',
        widget= forms.Textarea(
            attrs= {
                'class': 'form-control',
                'dir': 'rtl',
                'rows': '4',
            } 
        )
    )