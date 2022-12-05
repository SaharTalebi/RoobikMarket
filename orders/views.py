from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from dashboard.models import Address

# Create your views here.

@login_required
def checkout_view(request):
    default_address = Address.objects.filter(is_selected='true')
    return render(request, 'orders/checkout.html', {'default_address': default_address})
