from django.urls import path

from .views import UserRegisterView, UserLoginView, logout_user_view, UserAuthenticationView, ProfileSettingsView

urlpatterns = [
    path("authentication/", UserAuthenticationView.as_view(), name="authentication"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_user_view, name="logout"),
    path("settings/", ProfileSettingsView.as_view(), name="settings"),
]
