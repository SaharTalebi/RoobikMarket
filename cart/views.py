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
    print(product)

    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            quantity = cleaned_data['quantity']
            cart.add(product, quantity)
    return redirect('cart')

