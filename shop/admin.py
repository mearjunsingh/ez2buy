from django.contrib import admin
from shop.models import product,cart,category,order

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['id','name','thumbnail','price','offer_price','tags','quantity']

admin.site.register(product,productAdmin )


class cartAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'products' ,'quantity', 'is_checked']

admin.site.register(cart,cartAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = [ 'id','categorys','slug' ]

admin.site.register(category,categoryAdmin)

class orderAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'user','productss','ordered_at','is_completed']

admin.site.register(order,orderAdmin)
