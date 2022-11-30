from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Подтверждение пароля"}))

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2",)
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Email"}),
            "username": forms.TextInput(
                attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Имя пользователя"}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Пароль"}))
