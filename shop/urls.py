from django.urls import path
from shop.views import index_page, single_product_page

urlpatterns = [
    path('', index_page, name='index_page'),
    path('product/<str:slug>/', single_product_page, name='single_product_page'),
]