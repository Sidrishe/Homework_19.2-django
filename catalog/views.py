from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, View, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from catalog.models import Product, Version
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, VersionForm


# class HomeView(TemplateView):
#     template_name = 'catalog/product_list.html'
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['object_list'] = Product.objects.all()
#         return context_data


# def home(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Каталог товаров'
#     }
#     return render(request, 'catalog/product_list.html', context)

# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list.all(),
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/product_list.html', context)

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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):

        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


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
