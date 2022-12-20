from product.models import Product, Category

def base_view(request):
    mobiles = Category.objects.filter(parent__name='گوشی موبایل')
    voice = Category.objects.filter(parent__name='صوت')
    computers = Category.objects.filter(parent__name='کامپیوتر')
    videos = Category.objects.filter(parent__name='تصویر')
    furniture = Category.objects.filter(parent__name='مبلمان')
    decoration = Category.objects.filter(parent__name='دکوراسیون')
    men_clothing = Category.objects.filter(parent__name='پوشاک مردانه')
    ladies_clothing = Category.objects.filter(parent__name='پوشاک زنانه')


    context = {
        'mobiles': mobiles,
        'voices' : voice,
        'computers': computers,
        'videos' : videos,
        'furniture' : furniture,
        'decoration' : decoration,
        'men_clothing' : men_clothing,
        'ladies_clothing' : ladies_clothing,
    }
    return context