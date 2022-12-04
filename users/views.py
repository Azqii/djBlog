from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from .forms import UserRegisterForm, UserLoginForm, ProfileSettingsForm


class UserAuthentication(TemplateView):
    template_name = "users/authentication.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile", self.request.user.profile.id)
        return super(UserAuthentication, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserAuthentication, self).get_context_data(**kwargs)
        context["title"] = "Аутентификация"
        return context


class UserRegister(CreateView):
    form_class = UserRegisterForm


    def get(self, request, *args, **kwargs):
        return redirect("authentication")

    def get_success_url(self):
        return reverse_lazy("authentication")  # TODO: переделать на вход


class UserLogin(LoginView):
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        return redirect("authentication")

    def get_success_url(self):
        return reverse_lazy("feed")


def logout_user(request):
    logout(request)
    return redirect("authentication")


class ProfileSettings(FormView):
    template_name = "users/profile_settings.html"
    form_class = ProfileSettingsForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Настройки"
        return context


    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user

        initial.update({"first_name": user.first_name, "last_name": user.last_name,
                        "vk": user.profile.vk, "tg": user.profile.tg,
                        "instagram": user.profile.instagram, "bio": user.profile.bio,
                        "photo": user.profile.photo})
        return initial

    def form_valid(self, form):
        form = form.cleaned_data
        user = self.request.user

        user.profile.photo = form["photo"]
        user.first_name = form["first_name"]
        user.last_name = form["last_name"]
        user.profile.vk = form["vk"]
        user.profile.tg = form["tg"]
        user.profile.instagram = form["instagram"]
        user.profile.bio = form["bio"]
        user.save()

        return redirect("profile", user.profile.id)

