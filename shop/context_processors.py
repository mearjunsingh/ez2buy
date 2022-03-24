from shop.models import Cart, Category

def cart_count(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user, is_checked_out=False).count()
    else:
        cart_count = 0
    context = {
        'cart_count' : cart_count
    }
    return context
    

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return context