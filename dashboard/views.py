from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonalInfoForm, AddressForm
from .models import Address
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
    user = request.user
    addresses = Address.objects.filter(person=user)
    address_form = AddressForm(request.POST or None)

    if request.method == "POST":
        if address_form.is_valid:
            state = request.POST['state']
            city = request.POST['city']
            full_address = request.POST['full_address']
            postal_code = request.POST['postal_code']
            phone_no = request.POST['phone_no']
            delivery_person = request.POST['delivery_person']
            new_address = Address.objects.create(person=user, state=state, city=city, full_address=full_address, postal_code=postal_code,
                                                 phone_no=phone_no, delivery_person=delivery_person)
            new_address.save()
            return redirect('addresses')
    context = {
        'addresses': addresses,
        'address_form': address_form,
    }
    return render(request, 'dashboard/addresses.html', context)

def delete_address_view(request, id):
    address = get_object_or_404(Address, id=id)
    address.delete()
    return redirect('addresses')

def edit_address_view(request, id):
    user = request.user
    addresses = Address.objects.filter(person=user)
    address = get_object_or_404(Address, id=id)
    form = AddressForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            state = request.POST['state']
            city = request.POST['city']
            full_address = request.POST['full_address']
            phone_no = request.POST['phone_no']
            postal_code = request.POST['postal_code']
            delivery_person = request.POST['delivery_person']
            Address.objects.filter(id=id).update(state=state, city=city, full_address=full_address, phone_no=phone_no,
                                                delivery_person=delivery_person, postal_code=postal_code,)
            return redirect('addresses')

    context = {
        'addresses': addresses,
        'address': address,
    }
    return render(request, 'dashboard/edit_address.html', context)

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

    return redirect(request.META.get('HTTP_REFERER', '/'))
                
    
    

