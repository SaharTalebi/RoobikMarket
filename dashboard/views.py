from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import PersonalInfoForm
from accounts.models import CustomUser
from product.models import Product


def personal_info_view(request):
    user = request.user
    personal_info = CustomUser.objects.filter(username=user)
    form = PersonalInfoForm(initial={'username': user,})
    page_type = request.GET.get('type', '')
    context = {
        'form': form,
        'form_field': page_type,
        'personal_info': personal_info,
    }
    if page_type == 'edit':
        return render(request, 'dashboard/edit_info.html', context)

    return render(request, 'dashboard/personal_info.html', context)


def edit_personal_info_view(request):
    user = request.user
    form = PersonalInfoForm(request.POST or None, initial={'username': user})
    if request.method == 'POST':
        if form.is_valid:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            cart_number = request.POST['cart_number']
            phone_number = request.POST['phone_number']
            p_id = request.POST['p_id']
            email = request.POST['email']
            CustomUser.objects.filter(username=user).update(
                                    email=email, first_name=first_name, last_name=last_name, p_id=p_id,
                                    cart_no=cart_number, phone_no=phone_number)

    return redirect('personal_info')

def address_view(request):
    return render(request, 'dashboard/addresses.html')

def factors_view(request):
    return render(request, 'dashboard/factors.html')

def favorites_view(request):
    fav_product = Product.objects.filter(user_wishlist=request.user)
    context = {
        'fav_product': fav_product,
    }
    return render(request, 'dashboard/favorits.html', context)

def fav_product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
    else:
        product.user_wishlist.add(request.user)
    # return HttpResponseRedirect(request.META["HTTP_REFERE"])
    return redirect(request.build_absolute_uri())
                
    
    

