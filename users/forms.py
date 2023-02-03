from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2",)


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField()


class ProfileSettingsForm(forms.Form):
    photo = forms.ImageField(required=False)
    first_name = forms.CharField(required=False, max_length=150)
    last_name = forms.CharField(required=False, max_length=150)
    vk = forms.CharField(required=False, max_length=100)
    tg = forms.CharField(required=False, max_length=100)
    instagram = forms.CharField(required=False, max_length=100)
    bio = forms.CharField(required=False, widget=forms.Textarea())
