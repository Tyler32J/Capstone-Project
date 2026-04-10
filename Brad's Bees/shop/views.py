from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from decimal import Decimal
from .models import Product

def store_view(request):
    """Display all products in the shop"""
    products = Product.objects.all()
    context = {
        'products': products,
        'cart_count': len(request.session.get('cart', {}))
    }
    return render(request, 'shop.html', context)

def add_to_cart(request, product_id):
    """Add a product to the shopping cart (session-based)"""
    product = get_object_or_404(Product, id=product_id)
    
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    product_key = str(product_id)
    
    if product_key in cart:
        cart[product_key]['quantity'] += 1
    else:
        cart[product_key] = {
            'name': product.name,
            'variant': product.variant or '',
            'price': float(product.price) if product.price else 0,
            'quantity': 1,
            'image': product.image.url if product.image else ''
        }
    
    request.session.modified = True
    
    # Return JSON if AJAX request, otherwise redirect
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': sum(item['quantity'] for item in cart.values())
        })
    
    return redirect('cart')

def cart_view(request):
    """Display the shopping cart"""
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = Decimal('0')
    
    for product_id, item in cart.items():
        item_total = Decimal(str(item['price'])) * item['quantity']
        subtotal += item_total
        cart_items.append({
            'id': product_id,
            'name': item['name'],
            'variant': item['variant'],
            'price': item['price'],
            'quantity': item['quantity'],
            'image': item['image'],
            'total': float(item_total)
        })
    
    # Calculate shipping (example: free over $50, $5 otherwise)
    shipping = Decimal('0') if subtotal > 50 else Decimal('5')
    total = subtotal + shipping
    
    context = {
        'cart_items': cart_items,
        'subtotal': f"{subtotal:.2f}",
        'shipping': f"{shipping:.2f}",
        'total': f"{total:.2f}",
        'cart_count': len(cart)
    }
    return render(request, 'cart.html', context)

def remove_from_cart(request, product_id):
    """Remove an item from the shopping cart"""
    cart = request.session.get('cart', {})
    product_key = str(product_id)
    
    if product_key in cart:
        del cart[product_key]
        request.session.modified = True
    
    return redirect('cart')

def update_cart(request, product_id):
    """Update the quantity of an item in the cart"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        product_key = str(product_id)
        
        if product_key in cart:
            if quantity > 0:
                cart[product_key]['quantity'] = quantity
            else:
                del cart[product_key]
            request.session.modified = True
    
    return redirect('cart')

# --- Checkout View ---
def checkout_view(request):
    """Display the checkout page."""
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')
    subtotal = sum(float(item['price']) * item['quantity'] for item in cart.values())
    shipping = 0 if subtotal > 50 else 5
    total = subtotal + shipping
    context = {
        'cart_items': cart,
        'subtotal': f"{subtotal:.2f}",
        'shipping': f"{shipping:.2f}",
        'total': f"{total:.2f}",
        'cart_count': len(cart)
    }
    return render(request, 'checkout.html', context)
