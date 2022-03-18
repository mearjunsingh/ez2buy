from unicodedata import category
from django.shortcuts import redirect, render
from shop.models import Product, Order, Cart, Category


# def index_page(request):
#     index = Product.objects.all()
#     context_data = {
#         'index' : index
#     }
#     return render(request, 'index.html', context_data )

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


def add_to_cart(request, slug):
    cart = Cart()
    cart.user = request.user
    cart.product = Product.objects.get(slug=slug)
    cart.quantity = request.POST.get('quantity')
    cart.is_checked_out = False
    cart.save()
    return redirect(f'/product/{slug}')

def carts(request,slug):
    cart = Cart.objects.get(slug=slug)
    context = {
        'cart' : cart
    }
    return render(request, 'cart.html', context)

def dashboard(request,slug):
    order = Order()
    order = Order.objects.get(slug=slug)
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