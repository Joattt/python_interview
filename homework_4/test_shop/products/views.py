from products.models import Products
from products.forms import ProductsForm
from django.views.generic import FormView, ListView, CreateView
from django.urls import reverse_lazy


class ProductsListView(ListView, FormView):
    form_class = ProductsForm
    template_name = 'goods_list.html'
    queryset = Products.objects.all()


class ProductsAddView(CreateView, FormView):
    form_class = ProductsForm
    template_name = 'good_create.html'
    success_url = reverse_lazy('products_index')
