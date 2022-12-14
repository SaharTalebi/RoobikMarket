from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from .forms import ContactUsForm
from blog.models import BlogPost
from product.models import Product

# Create your views here.

def home_page_view(request):
    query = request.GET.get('query', '')
    
    featured_products = Product.active_product.filter(
        featured_category__name='محصولات منتخب').filter( 
        Q(title__icontains=query) | Q(description__icontains=query))[0:4]

    on_sale_products = Product.active_product.filter(
        featured_category__name='تخفیف خورده').filter(
        Q(title__icontains=query) | Q(description__icontains=query))[0:4]

    most_visited_products = Product.active_product.filter(
        featured_category__name='پربازدیدترین').filter( 
        Q(title__icontains=query) | Q(description__icontains=query))[0:4]

    special_sale_products = Product.active_product.filter(
        featured_category__name='تخفیف خورده').filter( 
        Q(title__icontains=query) | Q(description__icontains=query))[0:2]

    most_sale_mobiles = Product.active_product.filter(
        featured_category__name='پرفروش ترین', category__name='گوشی موبایل').filter( 
        Q(title__icontains=query) | Q(description__icontains=query))

    most_sale_laptops = Product.active_product.filter(
        featured_category__name='پرفروش ترین', category__name='لب تاپ').filter( 
        Q(title__icontains=query) | Q(description__icontains=query))

    most_sale_computer_accessories = Product.active_product.filter(
        featured_category__name='پرفروش ترین', category__name='جانبی کامپیوتر').filter( 
        Q(title__icontains=query) | Q(description__icontains=query))

    most_sale_cameras = Product.active_product.filter(
        featured_category__name='پرفروش ترین', category__name='دوربین').filter( 
        Q(title__icontains=query) | Q(description__icontains=query))

    blog_posts = BlogPost.objects.filter(is_active=True)[0:3]

    if request.user.is_authenticated:
        fav_product = Product.active_product.filter(user_wishlist=request.user)
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

class FaqView(generic.TemplateView):
    template_name = 'pages/faq.html'

class Error404View(generic.TemplateView):
    template_name = 'pages/error404.html'

class AboutUsView(generic.TemplateView):
    template_name = 'pages/about.html'