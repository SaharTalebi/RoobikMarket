from django import forms
from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm, ResetPasswordForm

from .models import CustomUser


class CustomUserResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserResetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['email'] = forms.EmailField(
        label="پست الکترونیک",
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                # "placeholder": "پست الکترونیک",
                "autocomplete": "email",
            }
        ),
    )



class CustomUserChangePasswordForm(ChangePasswordForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['oldpassword'] = forms.CharField(
            label='رمز عبور فعلی :',
            widget=forms.PasswordInput()
        )
        self.fields['password1'] = forms.CharField(
            label='رمز عبور جدید :',
            widget=forms.PasswordInput()
        )
        self.fields['password2'] = forms.CharField(
            label=' تکرار رمز عبور جدید :',
            widget=forms.PasswordInput( )
        )


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
            widget=forms.PasswordInput()
        )


class CustomUserSignupForm(SignupForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'] = forms.CharField(
            label='پست الکترونیک:',
            widget=forms.EmailInput()
        )
        self.fields['password1'] = forms.CharField(
            label='رمز عبور:',
            widget=forms.PasswordInput()
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



