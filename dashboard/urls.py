from django.urls import path

from . import views

urlpatterns = [
    path('', views.personal_info_view, name='personal_info'),
    path('edit_info/', views.edit_personal_info_view, name='edit_info'),
]

