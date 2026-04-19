from django.contrib import admin
from .models import Product, Cart, Item, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'variant', 'price', 'stock', 'rating']
    list_filter = ['rating', 'stock']
    search_fields = ['name', 'variant', 'description']
    fields = ['name', 'variant', 'description', 'price', 'stock', 'image', 'rating']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'session_key', 'created_at', 'grand_total']
    search_fields = ['user__username', 'session_key']
    readonly_fields = ['created_at']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'total_price']
    readonly_fields = ['total_price']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'unit_price', 'line_total']
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'total', 'created_at']
    list_filter = ['created_at', 'state', 'city']
    search_fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'zip_code']
    readonly_fields = ['subtotal', 'shipping', 'total', 'created_at']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'unit_price', 'line_total']
    list_filter = ['order__created_at']
    search_fields = ['order__id', 'product__name']
