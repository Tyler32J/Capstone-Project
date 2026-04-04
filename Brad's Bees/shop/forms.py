from django import forms
from django.forms import ModelForm
from .models import *

class ProductForm(forms.ModelForm): # for admin side, adding new products or updating them
    class Meta:
        model = Product
        fields = [
            'name',
            'variant',
            'description',
            'price',
            'stock',
        ]
    name = forms.CharField(max_length=30, required=True)
    variant = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=999, required=True)
    price = forms.DecimalField(max_digits=2, required=True)
    stock = forms.IntegerField(min_value=0, max_value=999, required=True)



class AddItemForm(forms.ModelForm): # for cart, user side
    class Meta:
        model = Item
        fields = [
            'quantity',
        ]
    quantity = forms.IntegerField(min_value=1, initial=1)