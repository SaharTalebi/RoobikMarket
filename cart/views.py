from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import AddToCartForm
from product.models import Product

# Create your views here.

def cart_view(request):
    cart = Cart(request)
    for item in cart:
        item['add_to_cart_form'] = AddToCartForm(initial={'quantity': item['quantity'], 'replace_quantity': True,})
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context)

def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            cart.add(product, quantity)
    return redirect('cart:cart')

def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart')

def empty_cart_view(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart')

def change_cart_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            replace_quantity = cleaned_data['replace_quantity']
            cart.add(product, quantity, replace_quantity)
    return redirect('cart:cart')



