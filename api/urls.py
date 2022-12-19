from django.urls import path

from .views import BlogPostView, BlogPostDetailView, UsersListView, UserDetailView

urlpatterns = [
    path('/', BlogPostView.as_view(), name='blog_list'),
    path('/<int:pk>', BlogPostDetailView.as_view(), name='blog_detail'),
    path('/users', UsersListView.as_view(), name="users_list"),
    path('/users/<int:pk>', UserDetailView.as_view(), name="user_detail"),
]
