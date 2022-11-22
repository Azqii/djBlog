from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm, UserLoginForm


class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"

    def get_context_data(self, **kwargs):
        context = super(UserRegister, self).get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super(UserLogin, self).get_context_data()
        context["title"] = "Авторизация"
        return context

    def get_success_url(self):
        return reverse_lazy("feed")


def logout_user(request):
    logout(request)
    return redirect("login")
