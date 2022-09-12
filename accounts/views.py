from .forms import MyCustomSignupForm, MyCustomLoginForm
from allauth.account.views import SignupView, LoginView
from django.urls import reverse_lazy

class MyCustomLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = MyCustomLoginForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(MyCustomLoginView, self).get_context_data(**kwargs)
        LogInForm = MyCustomLoginForm(self.request.POST or None)
        context['form'] = LogInForm
        return context

class MyCustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = MyCustomSignupForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(MyCustomSignupForm, self).get_context_data(**kwargs)
        SignupForm = MyCustomSignupForm(self.request.POST or None)
        context['form'] = SignupForm
        return context
