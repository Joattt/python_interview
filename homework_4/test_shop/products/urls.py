from django.urls import path
from products.views import ProductsListView, ProductsAddView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_index'),
    path('add/', ProductsAddView.as_view(), name='products_add'),
]
