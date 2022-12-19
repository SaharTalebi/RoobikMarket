from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import BlogPostSerializer, UsersSerializer
from .permissions import IsSuperUser, IsAdminUser
from accounts.models import CustomUser
from blog.models import BlogPost


class BlogPostView(ListAPIView):
    queryset = BlogPost.objects.filter(is_active=True).order_by('-datetime_created')
    serializer_class = BlogPostSerializer


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class UsersListView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser,)

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsSuperUser,)