from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from account.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1')


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    city = forms.CharField(label="Город", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}))
    avatar = forms.FileField(label="Аватар", widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}))

    class Meta:
        model = Profile
        fields = ['city', 'phone', 'avatar']
