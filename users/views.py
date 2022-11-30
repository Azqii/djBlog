from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import UserRegisterForm, UserLoginForm


class UserAuthentication(TemplateView):
    template_name = "users/authentication.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("feed")  # TODO: переписать на страницу пользователя
        return super(UserAuthentication, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserAuthentication, self).get_context_data(**kwargs)
        context["title"] = "Аутентификация"
        return context


class UserRegister(CreateView):
    form_class = UserRegisterForm

    def get(self, request, *args, **kwargs):
        return redirect("authentication")

    def get_context_data(self, **kwargs):
        context = super(UserRegister, self).get_context_data(**kwargs)
        context["register_form"] = context.get("form")
        return context

    def get_success_url(self):
        return reverse_lazy("authentication")


class UserLogin(LoginView):
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        return redirect("authentication")

    def get_context_data(self, **kwargs):
        context = super(UserLogin, self).get_context_data()
        context["login_form"] = context.get("form")
        return context

    def get_success_url(self):
        return reverse_lazy("feed")


def logout_user(request):
    logout(request)
    return redirect("authentication")
