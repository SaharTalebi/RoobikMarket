from django.shortcuts import render

# Create your views here.

def factors_view(request):
    return render(request, 'orders/factors.html')
