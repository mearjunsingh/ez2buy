from django.shortcuts import redirect, render
from user.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model


User = get_user_model()


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        context = {}

        form = LoginForm(request.POST or None)

        context['form'] = form

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request=request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                context['msg'] = 'invalid password'

        return render(request, 'create.html', context)


def logout_page(request):
    logout(request)
    return redirect('/')


def register_page(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'create.html', {'form' : form})