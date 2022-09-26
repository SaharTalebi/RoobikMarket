from django.urls import path

from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('products_list/', views.products_list_view, name='products_list'),
    # path('<int:pk>', views.product_detail_view, name='product_detail'),

]
