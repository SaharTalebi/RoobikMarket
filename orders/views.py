from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from dashboard.models import Address

# Create your views here.

@login_required
def checkout_view(request):
    default_address = Address.objects.filter(is_selected='true')
    context = {
        'default_address': default_address
        }
    if request.method == "POST":
        if default_address :
            messages(request, 'شما باید ابتدا یک آدرس برای خود ثبت کنید.')
        else:
            pass

    return render(request, 'orders/checkout.html', context)
