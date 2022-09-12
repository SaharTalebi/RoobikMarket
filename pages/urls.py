from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name="home"),
    path('about/', views.about_us_view, name="about"),
    path('contact/', views.contact_us_view, name="contact"),
    path('faq/', views.faq_view, name="faq"),
    path('error404/', views.error_404_view, name="error404"),
]
