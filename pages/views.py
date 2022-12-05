from django.shortcuts import render

from .forms import ContactUsForm
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

    if request.user.is_authenticated:
        fav_product = Product.objects.filter(user_wishlist=request.user)
    else: 
        fav_product = None
        
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
        'fav_product': fav_product,
        
    }
    return render(request, 'pages/home.html', context)

def contact_us_view(request):
    form = ContactUsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = ContactUsForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/contact.html', context)

def faq_view(request):
    return render(request, 'pages/faq.html')

def error_404_view(request):
    return render(request, 'pages/error404.html')

def about_us_view(request):
    return render(request, 'pages/about.html')