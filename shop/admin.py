from django.contrib import admin

from .models import Cart, Category, Order, Product

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Category)
