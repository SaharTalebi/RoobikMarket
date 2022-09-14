from django.shortcuts import render, get_object_or_404

from .models import BlogPost
# Create your views here.

def blog_list_view(request):
    blog_posts = BlogPost.objects.all().order_by('-datetime_created')
    context = {
        'posts': blog_posts,
    }
    return render(request, 'blog/blog.html', context)

def blog_post_detail_view(request, pk):
    post_detail = get_object_or_404(BlogPost, pk=pk)
    context = {
        'post_detail': post_detail,
    }
    return render(request, 'blog/blog_post_detail.html', context)
