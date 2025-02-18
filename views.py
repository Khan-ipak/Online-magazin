from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user)
    order.product.add(product)
    order.total_price += product.price
    order.save()
    return redirect('cart')

@login_required
def cart(request):
    order = Order.objects.filter(user=request.user).first()
    return render(request, 'store/cart.html', {'order': order})
