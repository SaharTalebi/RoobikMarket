from django.shortcuts import render, redirect

from .forms import PersonalInfoForm
from .models import PersonalInfo


def personal_info_view(request):
    user = request.user
    personal_info = PersonalInfo.objects.filter(person__username=user)
    form = PersonalInfoForm(initial={'person': user,})
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
    form = PersonalInfoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            cart_number = request.POST['cart_number']
            phone_number = request.POST['phone_number']
            p_id = request.POST['p_id']
            PersonalInfo.objects.filter(person=request.user).update(
                                        first_name=first_name, last_name=last_name, p_id=p_id,
                                        cart_number=cart_number, phone_number=phone_number)
    
    return redirect('personal_info')

