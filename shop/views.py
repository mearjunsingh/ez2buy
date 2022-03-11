from django.shortcuts import render
from shop.models import Product, Order, Cart, Category


def index_page(request):
    return render(request, 'index.html')


def single_product_page(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product' : product
    }
    return render(request, 'single.html', context)