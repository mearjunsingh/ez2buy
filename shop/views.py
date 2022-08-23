from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.db.models import Q

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


def cat_page(request, slug):
    products = Product.objects.filter(category__slug=slug)
    context = {"products": products}
    return render(request, "search.html", context)


def search_page(request):
    products = Product.objects.filter(active=True)
    query = request.GET.get("q")
    if query:
        products = products.filter(Q(name__icontains=query) | Q(tags__icontains=query))
    context = {"products": products}
    return render(request, "search.html", context)


def single_product_page(request, slug):
    product = Product.objects.get(slug=slug)
    recommended_products = Product.objects.filter(category=product.category).exclude(
        id=product.id
    )

    context = {
        "product": product,
        "recommended_products": recommended_products,
    }
    return render(request, "single.html", context)


@login_required(login_url="login_page")
def add_to_cart(request, slug):
    if request.method == "POST":
        product = Product.objects.get(slug=slug)
        quantity = int(request.POST.get("quantity"))
        if product.quantity >= quantity:
            try:
                cart = Cart.objects.get(
                    user=request.user, product=product, is_checked_out=False
                )
                cart.quantity += quantity
                product.quantity -= quantity
                product.save()
                cart.save()
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    user=request.user, product=product, quantity=quantity
                )
                product.quantity -= quantity
                product.save()
        return redirect(f"/product/{slug}")
    else:
        raise Http404


@login_required(login_url="login_page")
def carts_page(request):
    cart = Cart.objects.filter(user=request.user, is_checked_out=False)
    context = {"cart": cart}
    return render(request, "cart.html", context)


@login_required(login_url="login_page")
def user_dashboard(request):
    orders = Order.objects.filter(user=request.user)
    context = {"orders": orders}
    return render(request, "dashboard.html", context)


@login_required(login_url="login_page")
def checkout_page(request):
    cart = Cart.objects.filter(user=request.user, is_checked_out=False)
    total_amount = 0
    for item in cart:
        if item.product.offer_price:
            total_amount += item.product.offer_price * item.quantity
        else:
            total_amount += item.product.price * item.quantity

    context = {"cart": cart, "total_amount": total_amount}
    return render(request, "checkout.html", context)


@login_required(login_url="login_page")
def complete_checkout(request):
    cart = Cart.objects.filter(user=request.user, is_checked_out=False)
    for item in cart:
        item.is_checked_out = True
        item.save()
        Order.objects.create(
            user=request.user, product=item.product, quantity=item.quantity
        )
    return redirect("user_dashboard")
