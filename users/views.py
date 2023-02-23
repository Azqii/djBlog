from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, FormView

from .forms import UserRegisterForm, ProfileSettingsForm, UserLoginForm
from .utils import AuthenticationFormsMixin
from .services import save_user_profile_info, get_user_info


class UserAuthenticationView(TemplateView):
    """View аутентификации пользователей"""
    template_name = "users/authentication.html"
    extra_context = {"title": "Аутентификация"}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile", self.request.user.profile.id)
        return super().get(request, *args, **kwargs)


class UserRegisterView(AuthenticationFormsMixin, CreateView):
    """
    View для регистрации нового пользователя.

    Работает только с методом POST в запросе, форма передается через templatetags.
    """
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse("authentication")


class UserLoginView(AuthenticationFormsMixin, LoginView):
    """
    View для аутентификации пользователей.

    Работает только с методом POST в запросе, форма передается через templatetags.
    """
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse("feed")


def logout_user_view(request):
    """View завершения сессии пользователем."""
    logout(request)
    return redirect("authentication")


class ProfileSettingsView(LoginRequiredMixin, FormView):
    """View настроек информации о пользователе."""
    template_name = "users/profile_settings.html"
    form_class = ProfileSettingsForm
    extra_context = {"title": "Настройки"}

    def get_initial(self):
        initial = super().get_initial()
        initial.update(get_user_info(self.request.user))
        return initial

    def form_valid(self, form):
        save_user_profile_info(user=self.request.user, info=form.cleaned_data)
        return redirect("profile", self.request.user.profile.id)
