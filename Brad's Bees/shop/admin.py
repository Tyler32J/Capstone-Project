from django.contrib import admin
from .models import Product, Cart, Item

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'variant', 'price', 'stock', 'rating']
    list_filter = ['rating', 'stock']
    search_fields = ['name', 'variant', 'description']
    fields = ['name', 'variant', 'description', 'price', 'stock', 'image', 'rating']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'grand_total']
    readonly_fields = ['created_at']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'total_price']
    readonly_fields = ['total_price']
