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

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    address_line_1 = forms.CharField(max_length=255, label="Address")
    address_line_2 = forms.CharField(
        max_length=255,
        required=False,
        label="Apartment, suite, etc. (optional)",
    )
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=20, label="ZIP Code")
    notes = forms.CharField(widget=forms.Textarea, required=False)