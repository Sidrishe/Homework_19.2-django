from django.urls import path

from catalog.views import contacts, HomeView, ProductListView, ProductDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts, name='contact'),
    path('<int:pk>/product/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
