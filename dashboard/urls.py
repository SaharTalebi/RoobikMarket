from django.urls import path

from . import views

urlpatterns = [
    path('', views.personal_info_view, name='personal_info'),
    path('edit_info/', views.edit_personal_info_view, name='edit_info'),
    path('addresses/', views.address_view, name='addresses'),
    path('delete_address/<int:id>/', views.delete_address_view, name='del_address'),
    path('edit_address/<int:id>/', views.edit_address_view, name='edit_address'),
    path('favorites/', views.favorites_view, name='favorits'),
    path('fav-product/<int:product_id>', views.fav_product_view, name='fav_product'),

]

