from django.db import models
from django.conf import settings
from app.models import *


class Product(models.Model):
    name = models.CharField(max_length=30)
    variant = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=999)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    rating = models.FloatField(default=5.0)

    def __str__(self):
        if self.variant:
            return self.variant + self.name
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="carts",
    )
    session_key = models.CharField(max_length=40, null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def grand_total(self):
        return sum(item.total_price() for item in self.items.all())



class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("product", "cart")

    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        variant = (f" {self.product.variant}") if self.product.variant else ""
        return (f"{self.quantity} x {variant} {self.product.name}")


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} x {self.quantity}"