from django.views import generic
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import BlogPost, BlogComment
# Create your views here.

class BlogListView(generic.ListView):
    queryset = BlogPost.objects.all().order_by('-datetime_created')
    template_name = 'blog/blog.html'
    context_object_name = 'posts'


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
