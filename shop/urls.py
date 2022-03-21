from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import index_page, single_product_page, add_to_cart, carts, dashboard, checkout_page

urlpatterns = [
    path('', index_page, name='index_page'),
    path('product/<str:slug>/', single_product_page, name='single_product_page'),
    path('add-to-cart/<str:slug>/', add_to_cart, name='add_to_cart'),
    path('carts/', carts, name='carts'),
    path('dashboard/<str:slug>/', dashboard, name='dashboard'),
    path('checkout/', checkout_page, name='checkout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)