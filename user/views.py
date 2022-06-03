from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm

User = get_user_model()


def login_page(request):
    if request.user.is_authenticated:
        return redirect("user_dashboard")
    form = LoginForm(request=request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user_cre = authenticate(username=username, password=password)
        login(request, user_cre)
        if "next" in request.POST:
            next_url = request.POST.get("next")
            return redirect(next_url)
        else:
            return redirect("user_dashboard")
    return render(request, "create.html", {"form": form})


def logout_page(request):
    logout(request)
    return redirect("index_page")


def register_page(request):
    if request.user.is_authenticated:
        return redirect("user_dashboard")
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("user_dashboard")
    return render(request, "create.html", {"form": form})
