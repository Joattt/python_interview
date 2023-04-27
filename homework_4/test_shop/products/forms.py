from django.forms import ModelForm
from products.models import Products


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
