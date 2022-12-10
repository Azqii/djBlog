from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    """
    User registration form with styles
    """
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
    """
    User authorization form with styles
    """
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control bg-transparent rounded-0 my-4", "placeholder": "Пароль"}))


class ProfileSettingsForm(forms.Form):
    photo = forms.ImageField(required=False, label="Фото", widget=forms.FileInput(
        attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0"}))

    first_name = forms.CharField(required=False, label="Имя", max_length=150, widget=forms.TextInput(
        attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0",
               "placeholder": "Иван"}))
    last_name = forms.CharField(required=False, label="Фамилия", max_length=150, widget=forms.TextInput(
        attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0",
               "placeholder": "Иванов"}))

    vk = forms.CharField(required=False, label="Вконтакте", max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0",
               "placeholder": "Ваш id в vk"}))
    tg = forms.CharField(required=False, label="Телеграм", max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0",
               "placeholder": "Ваш никнейм в telegram"}))
    instagram = forms.CharField(required=False, label="Инстаграм", max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0",
               "placeholder": "Ваш никнейм в instagram"}))
    bio = forms.CharField(required=False, label="О себе", widget=forms.Textarea(
        attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0",
               "placeholder": "Информация о себе"}))
