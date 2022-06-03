from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from .models import Cart, Category, Order, Product


def index_page(request):
    featured_products = Product.objects.filter(featured=True, active=False).order_by(
        "-id"
    )[:6]
    new_products = Product.objects.filter(featured=False, active=False).order_by("-id")[
        :12
    ]
    active_products = Product.objects.filter(featured=False, active=True).order_by(
        "-id"
    )[:12]
    context_data = {
        "featured_products": featured_products,
        "new_products": new_products,
        "active_products": active_products,
    }
    return render(request, "index.html", context_data)


def single_product_page(request, slug):
    product = Product.objects.get(slug=slug)
    context = {"product": product}
    return render(request, "single.html", context)


@login_required
def add_to_cart(request, slug):
    if request.method == "POST":
        product = Product.objects.get(slug=slug)
        quantity = int(request.POST.get("quantity"))
        try:
            cart = Cart.objects.get(
                user=request.user, product=product, is_checked_out=False
            )
            cart.quantity += quantity
            cart.save()
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                user=request.user, product=product, quantity=quantity
            )
        return redirect(f"/product/{slug}")
    else:
        raise Http404


@login_required
def carts_page(request):
    cart = Cart.objects.filter(user=request.user)
    context = {"cart": cart}
    return render(request, "cart.html", context)


@login_required
def user_dashboard(request):
    orders = Order.objects.filter(user=request.user)
    context = {"orders": orders}
    return render(request, "dashboard.html", context)


@login_required
def checkout_page(request):
    cart = Cart.objects.filter(user=request.user)
    context = {"cart": cart}
    return render(request, "checkout.html", context)
