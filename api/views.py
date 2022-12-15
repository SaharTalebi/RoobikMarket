from rest_framework.generics import ListCreateAPIView

from .serializers import BlogPostSerializer
from blog.models import BlogPost


class BlogPostView(ListCreateAPIView):
    queryset = BlogPost.objects.filter(is_active=True).order_by('-datetime_created')
    serializer_class = BlogPostSerializer