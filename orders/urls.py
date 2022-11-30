from django.urls import path

from . import views

urlpatterns = [
    path('factors/', views.factors_view, name='factors'),
]
