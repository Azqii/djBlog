from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2", )
