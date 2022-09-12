from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'pages/home.html')

def about_us_view(request):
    return render(request, 'pages/about.html')

def contact_us_view(request):
    return render(request, 'pages/contact.html')

def faq_view(request):
    return render(request, 'pages/faq.html')

def error_404_view(request):
    return render(request, 'pages/error404.html')