from django.shortcuts import render

from .models import Product
# Create your views here.

def products_view(request):
    products = Product.objects.all().order_by('-datetime_created')
    context = {
        'products': products,
    }
    return render(request, 'product/products.html', context)

def products_list_view(request):
    products = Product.objects.all().order_by('-datetime_created')
    context = {
        'products': products,
    }
    return render(request, 'product/products_list.html', context)

# def product_detail_view(request):
#     return render(request, 'product/product_detail.html')
