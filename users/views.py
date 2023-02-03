from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from .forms import UserRegisterForm, ProfileSettingsForm, UserLoginForm
from .utils import AuthenticationMixin


class UserAuthenticationView(TemplateView):
    template_name = "users/authentication.html"
    extra_context = {"title": "Аутентификация"}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile", self.request.user.profile.id)
        return super().get(request, *args, **kwargs)


class UserRegisterView(AuthenticationMixin, CreateView):
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse_lazy("authentication")


class UserLoginView(AuthenticationMixin, LoginView):
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy("feed")


def logout_user(request):
    logout(request)
    return redirect("authentication")


class ProfileSettingsView(LoginRequiredMixin, FormView):
    template_name = "users/profile_settings.html"
    form_class = ProfileSettingsForm
    extra_context = {"title": "Настройки"}

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user

        initial.update({
            "first_name": user.first_name, "last_name": user.last_name,
            "vk": user.profile.vk, "tg": user.profile.tg,
            "instagram": user.profile.instagram, "bio": user.profile.bio,
            "photo": user.profile.photo
        })
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
