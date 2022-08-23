from django.urls import include, path

from .views import *

urlpatterns = [
    path("", index_page, name="index_page"),
    path("product/<str:slug>/", single_product_page, name="single_product_page"),
    path("add-to-cart/<str:slug>/", add_to_cart, name="add_to_cart"),
    path("carts/", carts_page, name="carts_page"),
    path("dashboard/", user_dashboard, name="user_dashboard"),
    path("checkout/", checkout_page, name="checkout"),
    path("search/", search_page, name="search_page"),
    path("cat/<str:slug>/", cat_page, name="cat_page"),
    path("complete-checkout/", complete_checkout, name="complete_checkout"),
]
