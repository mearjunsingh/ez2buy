from .models import Cart, Category


def cart_count(request):
    context = {}
    context["cart_count"] = None

    if request.user.is_authenticated:
        context["cart_count"] = Cart.objects.filter(
            user=request.user, is_checked_out=False
        ).count()

    return context


def categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return context
