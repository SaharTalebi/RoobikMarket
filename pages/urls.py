from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name="home"),
    path('contact/', views.contact_us_view, name="contact"),
    path('faq/', views.FaqView.as_view(), name="faq"),
    path('about/', views.AboutUsView.as_view(), name="about"),
    path('error404/', views.Error404View.as_view(), name="error404"),
]
