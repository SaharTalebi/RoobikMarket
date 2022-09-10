from django import forms
from allauth.account.forms import LoginForm, SignupForm

class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(
            label='نام کاربری :',
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    # 'placeholder': 'نام کاربری',
                    'dir': 'rtl',
                    'autocomplete': 'off'
                }
            ),
        )

        self.fields['password1'] = forms.CharField(
            label='رمز عبور :',
            widget=forms.PasswordInput(
                attrs={
                    'class': "form-control",
                    # 'placeholder': 'پسوورد',
                    'dir': 'rtl',
                    'autocomplete': 'off',
                }
            )
        )
    def save(self, request=None):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomLoginForm, self).save(request)
        # Add your own processing here.
        print(user.username)
        # You must return the original result.
        return user


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(
            label='نام کاربری',
            required= False,
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    # 'placeholder': 'نام کاربری',
                    'dir': 'rtl',
                    'autocomplete': 'off'
                }
            ),
        )
        self.fields['email'] = forms.EmailField(
            label='پست الکترونیک',
            widget=forms.EmailInput(
                attrs={
                    'class': "form-control",
                    # 'placeholder': 'ایمیل',
                    'dir': 'rtl',
                    'autocomplete':'off',
                    'required': 'True'
                },  
            )
        )
        self.fields['password1'] = forms.CharField(
            label='رمز عبور',
            widget=forms.PasswordInput(
                attrs={
                    'class': "form-control",
                    # 'placeholder': 'پسوورد',
                    'dir': 'rtl',
                    'autocomplete': 'off',
                }
            )
        )
        self.fields['password2'] = forms.CharField(
            label='تکرار رمز عبور',
            widget=forms.PasswordInput(
                attrs={
                    'class': "form-control",
                    # 'placeholder': 'تکرار پسوورد',
                    'dir': 'rtl',
                    'autocomplete': 'off',
                }
            )
        )


    def save(self, request=None):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        # Add your own processing here.
        print(user.username)
        # You must return the original result.
        return user
