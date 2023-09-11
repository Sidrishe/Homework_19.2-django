from django.urls import path

from catalog.views import home, contacts,  product

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts),
    path('<int:pk>/product/', product, name='product'),
]
