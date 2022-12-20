from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('<int:pk>', views.blog_post_detail_view, name='blog_post_detail'),
]
