from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    """Форма регистрации"""

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2",)


class UserLoginForm(AuthenticationForm):
    """Форма аутентификация"""
    username = forms.EmailField()


class ProfileSettingsForm(forms.Form):
    """
    Форма для настроек информации в профиле пользователя.

    Объединены некоторые поля из моделей User и Profile
    """
    photo = forms.ImageField(required=False)
    first_name = forms.CharField(required=False, max_length=150)
    last_name = forms.CharField(required=False, max_length=150)
    vk = forms.CharField(required=False, max_length=100)
    tg = forms.CharField(required=False, max_length=100)
    instagram = forms.CharField(required=False, max_length=100)
    bio = forms.CharField(required=False, widget=forms.Textarea())
