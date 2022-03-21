from django.shortcuts import redirect, render
from shop.models import Product, Order, Cart, Category
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required


def index_page(request):
    index = Product.objects.all()
    context_data = {
        'index' : index
    }
    return render(request, 'index.html', context_data )


def single_product_page(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product' : product
    }
    return render(request, 'single.html', context)


@login_required
def add_to_cart(request, slug):
    if request.method == 'POST':  
        cart = Cart()
        cart.user = request.user
        cart.product = Product.objects.get(slug=slug)
        cart.quantity = request.POST.get('quantity')
        cart.is_checked_out = False
        cart.save()
        return redirect(f'/product/{slug}')
    return HttpResponseNotFound()


def carts(request):
    cart = Cart.objects.filter(user=request.user)
    context = {
        'cart' : cart
    }
    return render(request, 'cart.html', context)


def dashboard(request):
    order = Order()
    # order = Order.objects.get(slug=slug)
    context = {
        'order' : order
    }
    return render(request, 'dashboard.html', context)

def checkout_page(request):
    cart = Cart.objects.filter(user=request.user)
    context = {
        'cart' : cart
    }
    return render(request, 'checkout.html', context)