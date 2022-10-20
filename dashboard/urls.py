from django.urls import path

from . import views

urlpatterns = [
    path('', views.personal_info_view, name='personal_info'),
]

