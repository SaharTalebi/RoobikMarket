from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .forms import ProductCommentForm
from .models import Product, ProductComment, Category


def products_view(request):
    page_type = request.GET.get('type', 'tile')
    page_value = request.GET.get('value', 'newest')
    products = Product.active_product.all()
    categories = Category.objects.filter(parent=None)

    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    if request.method == "POST":
        my_checkbox_list = request.POST.getlist('mycheckbox')

        if 'کالای دیجیتال' in my_checkbox_list:
            digit_list = Category.objects.filter(Q(name='کالای دیجیتال') | Q(parent__name='کالای دیجیتال') | Q(parent__name__in=['صوت','تصویر','کامپیوتر','گوشی موبایل'])).values_list('name')
            products = Product.active_product.filter(category__name__in = digit_list)

        elif 'مد و پوشاک' in my_checkbox_list:
            cloth_list = Category.objects.filter(Q(name='مد و پوشاک') | Q(parent__name='مد و پوشاک')).values_list('name')
            products = Product.active_product.filter(category__name__in = cloth_list)

        elif 'فرهنگ و هنر' in my_checkbox_list:
            art_list = Category.objects.filter(Q(name='فرهنگ و هنر') | Q(parent__name='فرهنگ و هنر')).values_list('name')
            products = Product.active_product.filter(category__name__in = art_list)

        elif 'سلامت و زیبایی' in my_checkbox_list:
            health_list = Category.objects.filter(Q(name='سلامت و زیبایی') | Q(parent__name='سلامت و زیبایی')).values_list('name')
            products = Product.active_product.filter(category__name__in = health_list)

        elif 'لوازم منزل' in my_checkbox_list:
            decor_list = Category.objects.filter(Q(name='لوازم منزل') | Q(parent__name='لوازم منزل')).values_list('name')
            products = Product.active_product.filter(category__name__in = decor_list)

        elif 'جواهرات' in my_checkbox_list:
            jwel_list = Category.objects.filter(Q(name='جواهرات') | Q(parent__name='جواهرات')).values_list('name')
            products = Product.active_product.filter(category__name__in = jwel_list)

        else:
            products = Product.active_product.all()

    if page_value == 'newest':    
        context = {
            'products': products,
            'categories': categories,
        }

    if page_value == 'most_visited':
        most_visited_products = Product.objects.filter(featured_category__name='پربازدیدترین')
        context = {
            'products': most_visited_products,
            'categories': categories,
        }

    if page_value == 'most_sale':
        most_sale_products = Product.objects.filter(featured_category__name='پرفروش ترین')
        context = {
            'products': most_sale_products,
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
    fav_product = Product.objects.filter(user_wishlist=request.user)

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
        'fav_product': fav_product,
    }
    return render(request, 'product/product_detail.html', context)
