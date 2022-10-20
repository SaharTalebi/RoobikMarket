from django.shortcuts import render

# Create your views here.

def personal_info_view(request):
    context = {
    }
    return render(request, 'dashboard/personal_info.html', context)
