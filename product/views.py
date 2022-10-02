from django.shortcuts import render, get_object_or_404

from .models import Product, ProductComment
from .forms import ProductCommentForm
# Create your views here.

def products_view(request):
    products = Product.objects.all().order_by('-datetime_created')
    context = {
        'products': products,
    }
    return render(request, 'product/products.html', context)

def products_list_view(request):
    products = Product.objects.all().order_by('-datetime_created')
    
    context = {
        'products': products,
    }
    return render(request, 'product/products_list.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_comment = ProductComment.objects.order_by('-datetime_created').filter(product=product)
    comment_form = ProductCommentForm(request.POST or None)

    if request.method == 'POST':
        if comment_form.is_valid:
            comment_body = request.POST['comment_body']
            author = request.user
            new_product_comment = ProductComment(author=author, product=product, comment_body=comment_body)
            new_product_comment.save()
            comment_form = ProductCommentForm()

    context = {
        'product': product,
        'comment_form': comment_form,
        'comments': product_comment,
    }
    return render(request, 'product/product_detail.html', context)
