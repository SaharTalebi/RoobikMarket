from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Product, ProductComment, Category
from .forms import ProductCommentForm
# Create your views here.

def products_view(request):
    page_type = request.GET.get('type', 'tile')
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(parent=None)

    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if request.method == "POST":
        my_checkbox_list = request.POST.getlist('mycheckbox')
        if 'کالای دیجیتال' in my_checkbox_list:
            products = Product.objects.filter(category__name='کالای دیجیتال', is_active=True)
        elif 'مد و پوشاک' in my_checkbox_list:
            products = Product.objects.filter(category__name='مد و پوشاک', is_active=True)
        elif 'فرهنگ و هنر' in my_checkbox_list:
            products = Product.objects.filter(category__name='فرهنگ و هنر', is_active=True)
        elif 'سلامت و زیبایی' in my_checkbox_list:
            products = Product.objects.filter(category__name='سلامت و زیبایی', is_active=True)
        elif 'لوازم منزل' in my_checkbox_list:
            products = Product.objects.filter(category__name='لوازم منزل', is_active=True)
        else:
            products = Product.objects.filter(is_active=True)
        
    context = {
        'products': products,
        'categories': categories,
    }

    if page_type == 'tile':
        return render(request, 'product/products.html', context)
    else:
        return render(request, 'product/products_list.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_comment = ProductComment.objects.filter(product=product, is_active=True)
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



# active_category = request.GET.get('category', '')
# if active_category:
# products = Product.objects.filter(category__name=active_category)