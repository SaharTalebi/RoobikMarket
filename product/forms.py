from socket import fromshare
from django import forms

from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('comment_body',)

    comment_body = forms.CharField(
        label= 'متن دیدگاه',
        widget= forms.Textarea(
            attrs = {
                'class': 'form-group my-1',
                'rows': '4',
            }
        )
    )
