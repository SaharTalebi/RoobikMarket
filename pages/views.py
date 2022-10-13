from django.shortcuts import render

from .forms import ContactUsForm
from .models import ContactUs
from product.models import Product
from blog.models import BlogPost


# Create your views here.

def home_page_view(request):
    featured_products = Product.objects.filter(featured_category__name='محصولات منتخب')[0:4]
    on_sale_products = Product.objects.filter(featured_category__name='تخفیف خورده')[0:4]
    most_visited_products = Product.objects.filter(featured_category__name='پربازدیدترین')[0:4]
    special_sale_products = Product.objects.filter(featured_category__name='تخفیف خورده')[0:2]
    most_sale_mobiles = Product.objects.filter(featured_category__name='پرفروش ترین', category__name='گوشی موبایل')
    most_sale_laptops = Product.objects.filter(featured_category__name='پرفروش ترین', category__name='لب تاپ')
    most_sale_computer_accessories = Product.objects.filter(featured_category__name='پرفروش ترین', category__name='جانبی کامپیوتر')
    most_sale_cameras = Product.objects.filter(featured_category__name='پرفروش ترین', category__name='دوربین')
    blog_posts = BlogPost.objects.filter(is_active=True)[0:3]

    context ={
        'featured_products': featured_products,
        'on_sale_products': on_sale_products,
        'most_visited_products': most_visited_products,
        'special_sale_products': special_sale_products,
        'most_sale_mobiles': most_sale_mobiles,
        'most_sale_laptops': most_sale_laptops,
        'most_sale_computer_accessories': most_sale_computer_accessories,
        'most_sale_cameras': most_sale_cameras,
        'blog_posts': blog_posts,
    }
    return render(request, 'pages/home.html', context)

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