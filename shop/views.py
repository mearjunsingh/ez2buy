from binascii import rledecode_hqx
from django.shortcuts import render
from shop.models import Product,Order,Cart,Category


# Create your views here.
def home_page(request):
    all = Product,Order,Cart,Category.objects.all()
    context = {
        'all' : all,
    }
    return render(request,'main.html',context)

def single_page(request,id):
    single = Product,Order,Cart,Category.objects.get(id=id)
    context = {
        'single' : single
    }
    return render(request,'single.html',context)