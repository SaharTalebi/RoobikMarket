from django.urls import path

from .views import BlogPostView, BlogPostDetailView

urlpatterns = [
    path('/', BlogPostView.as_view(), name='blog_list'),
    path('/<int:pk>', BlogPostDetailView.as_view(), name='blog_detail'),
]
