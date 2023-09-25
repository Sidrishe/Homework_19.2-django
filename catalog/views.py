from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


# def home(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Каталог товаров'
#     }
#     return render(request, 'catalog/home.html', context)

# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list.all(),
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/home.html', context)

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# def products(request, pk):
#     category_name = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category=pk),
#         'title': f'Каталог товаров - {category_name.name}'
#     }
#     return render(request, 'catalog/products.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'catalog/contacts.html')


# def product(request, pk):
#     products_item = Product.objects.get(pk=pk)
#     products_list = Product.objects.filter(pk=pk)
#     context = {
#         'object_list': products_list,
#         'title': f'Продукт - {products_item}'
#     }
#     return render(request, 'catalog/product_detail.html', context)
