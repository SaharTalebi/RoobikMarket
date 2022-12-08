from django import forms
from allauth.account.forms import LoginForm, SignupForm

from .models import CustomUser


class CustomUserLoginForm(LoginForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'] = forms.CharField(
            label='پست الکترونیک:',
            widget=forms.EmailInput(
                # attrs={
                #     'class': "form-control",
                #     # 'placeholder': 'ایمیل',
                #     'dir': 'rtl',
                #     'autocomplete':'off',
                #     'required': 'True'
                # },  
            )
        )
        self.fields['password'] = forms.CharField(
            label='رمز عبور:',
            widget=forms.PasswordInput(
                # attrs={
                #     'class': "form-control",
                #     'dir': 'rtl',
                #     'autocomplete': 'off',
                # }
            )
        )


class CustomUserSignupForm(SignupForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'] = forms.CharField(
            label='پست الکترونیک:',
            widget=forms.EmailInput(
                # attrs={
                #     'class': "form-control",
                #     'dir': 'rtl',
                #     'autocomplete':'off',
                #     'required': 'True'
                # },  
            )
        )
        self.fields['password1'] = forms.CharField(
            label='رمز عبور:',
            widget=forms.PasswordInput(
                # attrs={
                #     'class': "form-control",
                #     'dir': 'rtl',
                #     'autocomplete': 'off',
                # }
            )
        )
        self.fields['password2'] = forms.CharField(
            label='رمز عبور:',
            widget=forms.PasswordInput(
                # attrs={
                #     'class': "form-control",
                #     'dir': 'rtl',
                #     'autocomplete': 'off',
                # }
            )
        )



