from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerRegistrationForm, CustomerLoginForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация прошла успешно. Войдите в аккаунт !')
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('signup')
    else:
        form = CustomerRegistrationForm()

    context = {
        'form': form,
        'title': 'Регистрация пользователя'
    }
    return render(request, 'users/signup.html', context)


def user_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, 'Вы успешно авторизовались !')
                return redirect('index')
            else:
                messages.error(request, 'Не верное имя пользователя/пароль !')
                return redirect('login')
        else:
            messages.error(request, 'Не верное имя пользователя/пароль !')
            return redirect('login')
    else:
        form = CustomerLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)                       


def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('login')
