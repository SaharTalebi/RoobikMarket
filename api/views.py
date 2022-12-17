from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import BlogPostSerializer
from blog.models import BlogPost


class BlogPostView(ListAPIView):
    queryset = BlogPost.objects.filter(is_active=True).order_by('-datetime_created')
    serializer_class = BlogPostSerializer


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer