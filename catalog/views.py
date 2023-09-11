from django.shortcuts import render

from catalog.models import Product, Category


# def home(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Каталог товаров'
#     }
#     return render(request, 'catalog/home.html', context)

def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list.all(),
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def products(request, pk):
    category_name = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'Каталог товаров - {category_name.name}'
    }
    return render(request, 'catalog/products.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'catalog/contacts.html')


def product(request, pk):
    products_item = Product.objects.get(pk=pk)
    products_list = Product.objects.filter(pk=pk)
    context = {
        'object_list': products_list,
        'title': f'Продукт - {products_item}'
    }
    return render(request, 'catalog/cur_prod.html', context)
