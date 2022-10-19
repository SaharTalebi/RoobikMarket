from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart_view, name='cart_add'),
    path('remove/<int:product_id>', views.remove_from_cart_view, name='cart_remove'),
    path('empty', views.empty_cart_view, name='empty_cart'),
    path('change-quantity/<int:product_id>', views.change_cart_quantity, name='change_quantity'),
]
