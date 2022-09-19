from django.shortcuts import render, get_object_or_404

from .models import BlogPost, BlogComment
from .forms import CommentForm
# Create your views here.

def blog_list_view(request):
    blog_posts = BlogPost.objects.all().order_by('-datetime_created')
    context = {
        'posts': blog_posts,
    }
    return render(request, 'blog/blog.html', context)

def blog_post_detail_view(request, pk):
    post_detail = get_object_or_404(BlogPost, pk=pk)
    comments = BlogComment.objects.filter(post=post_detail).order_by('-datetime_created')
    comment_form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if comment_form.is_valid():
            author = request.user
            
            comment_body = request.POST['comment_body']
            new_comment = BlogComment(post=post_detail, author=author, comment_body=comment_body)
            new_comment.save()
            comment_form = CommentForm

    context = {
        'post_detail': post_detail,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_post_detail.html', context)
