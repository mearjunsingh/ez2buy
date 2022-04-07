from django.urls import path
from user.views import login_page, logout_page, register_page

urlpatterns = [
    path('', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('register/', register_page, name='register_page')
]