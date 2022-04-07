from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from shop import views as v

urlpatterns = [
    path('', v.index_page, name='index_page'),
    path('product/<str:slug>/', v.single_product_page, name='single_product_page'),
    path('add-to-cart/<str:slug>/', v.add_to_cart, name='add_to_cart'),
    path('carts/', v.carts_page, name='carts_page'),
    path('dashboard/', v.user_dashboard, name='user_dashboard'),
    path('checkout/', v.checkout_page, name='checkout'),
    path('', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)