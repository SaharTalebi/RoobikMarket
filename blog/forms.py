from django import forms


class CommentForm(forms.Form):

    # author = forms.CharField(
    #     label= 'نام شما',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'placeholder': '* نام شما',
    #             'required': 'True',
    #             'dir': 'rtl',
    #             'autocomplete': 'off',
    #         })
    # )
    # email= forms.EmailField(
    #     label= 'پست الکترونیک',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'placeholder': '* پست الکترونیک',
    #             'dir': 'rtl',
    #             'required': 'True',
    #             'autocomplete': 'off',
    #         })
    # )
    comment_body= forms.CharField(
        label= '',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 
                'dir': 'rtl',
                'rows': '4',
            })
    )