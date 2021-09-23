from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login, logout
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Вы успешно выполнили вход в систему')
            user = form.get_user()
            user_login(request, user)
            return redirect('/')
        else:
            # pass
            messages.error(request, 'Вы ввели некорректные данные')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/auth/login')
        else:
            # pass
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/auth/login')


def profile_edit(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Профиль обновлен успешно!')
            return redirect('profile')
    else:
        if not request.user.is_authenticated:
            return redirect('/auth/login')
        p_form = ProfileUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user.profile)

    context = {'p_form': p_form, 'u_form': u_form}
    return render(request, 'site_items/profile_edit.html', context)


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    list_profile = Profile.objects.filter(user__username=request.user)
    return render(
        request, 'site_items/profile.html',
        {
            'list_profile': list_profile,
            'title': 'Профиль'
        }
    )
