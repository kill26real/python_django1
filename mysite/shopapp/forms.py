from django import forms
from django.core import validators
from .models import Product, Order
from django.contrib.auth.models import User


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=10000, decimal_places=2)
#     description = forms.CharField(
#         label='Product description',
#         widget=forms.Textarea(attrs={'rows':8, 'cols': '30'}),
#         validators=[validators.RegexValidator(
#             regex='great',
#             message="Field mist contain word 'great'",
#         )],
#     )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'discount'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'user', 'delivery_adress', 'promocode', 'products'

# class OrderForm(forms.Form):
#     user = forms.CharField()
#     promocode = forms.CharField(max_length=100)
#     delivery_adress = forms.CharField(
#         label='Delivery adress',
#         widget=forms.Textarea(attrs={'rows':5, 'cols': '30'}),
#     )
#     products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())
