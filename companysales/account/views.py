from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login, logout
from .forms import UserLoginForm, UserRegisterForm
from .models import Profile


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # messages.success(request, 'Вы успешно выполнили вход в систему')
            user = form.get_user()
            user_login(request, user)
            return redirect('/')
        else:
            pass
            # messages.error(request, 'Вы ввели некорректные данные')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            # messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/auth/login')
        else:
            pass
    # messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/auth/login')
