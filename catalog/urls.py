from django.urls import path

from catalog.views import home, contacts, products, product

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts),
    path('products/', products, name='products'),
    path('<int:pk>/product/', product, name='product'),
]
