from django.contrib.auth.context_processors import auth
from django.shortcuts import render
from django.contrib import auth
from apps.users.forms import UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Личный кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
