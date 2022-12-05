from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PersonalInfoForm, AddressForm
from .models import Address
from accounts.models import CustomUser
from product.models import Product


@login_required
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


@login_required
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


@login_required
def address_view(request):
    user = request.user
    addresses = Address.objects.filter(person=user)
    address_form = AddressForm(request.POST or None)

    if request.method == "POST":
        default_address = request.POST['is_selected']

        if default_address == 'true':
            addresses.update(is_selected='false')

        if address_form.is_valid:
            new_address = address_form.save(commit=False)
            new_address.person = user
            new_address.save()
            return redirect('addresses')
    context = {
        'addresses': addresses,
        'address_form': address_form,
    }
    return render(request, 'dashboard/addresses.html', context)


@login_required
def delete_address_view(request, id):
    address = get_object_or_404(Address, id=id)
    address.delete()
    return redirect('addresses')


@login_required
def edit_address_view(request, id):
    user = request.user
    addresses = Address.objects.filter(person=user)
    address = get_object_or_404(Address, id=id)
    
    if request.method == "POST":
        form = AddressForm(request.POST)
        default_address = request.POST['is_selected']

        if default_address == 'true':
            addresses.exclude(id=id).update(is_selected='false')

        if form.is_valid():
            Address.objects.filter(id=id).update(
                city=request.POST['city'],
                state=request.POST['state'],
                phone_no=request.POST['phone_no'],
                is_selected=request.POST['is_selected'],
                postal_code=request.POST['postal_code'],
                full_address=request.POST['full_address'],
                delivery_person=request.POST['delivery_person'],
                )
            return redirect('addresses')

    context = {
        'addresses': addresses,
        'address': address,
    }
    return render(request, 'dashboard/edit_address.html', context)


@login_required
def favorites_view(request):
    fav_product = Product.objects.filter(user_wishlist=request.user)
    context = {
        'fav_product': fav_product,
    }
    return render(request, 'dashboard/favorits.html', context)


@login_required
def fav_product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
    else:
        product.user_wishlist.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def factors_view(request):
    return render(request, 'dashboard/factors.html')
                
    
    

