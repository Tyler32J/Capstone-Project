from django.db import models
from app.models import *

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    variant = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=999)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        if self.variant:
            return self.variant + self.name
        return self.name



class Cart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def grand_total(self):
        return sum(item.total_price() for item in self.items.all())



class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        variant = (f" {self.product.variant}") if self.product.variant else ""
        return (f"{self.quantity} x {variant} {self.product.name}")