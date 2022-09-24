from django.shortcuts import render

from .forms import ContactUsForm
from .models import ContactUs

# Create your views here.

def home_page_view(request):
    return render(request, 'pages/home.html')

def about_us_view(request):
    return render(request, 'pages/about.html')

def contact_us_view(request):
    form = ContactUsForm(request.POST or None)

    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['text']

        if form.is_valid():
            cantactus = ContactUs(name=name, phone=phone, email=email, subject=subject, text=text)
            cantactus.save()
            form = ContactUsForm

    context = {
        'form': form,
    }
    return render(request, 'pages/contact.html', context)

def faq_view(request):
    return render(request, 'pages/faq.html')

def error_404_view(request):
    return render(request, 'pages/error404.html')