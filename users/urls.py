from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

from .views import UserRegisterView, UserLoginView, logout_user_view, UserAuthenticationView, ProfileSettingsView
from .forms import CustomPasswordResetForm

urlpatterns = [
    path("authentication/", UserAuthenticationView.as_view(), name="authentication"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_user_view, name="logout"),
    path("settings/", ProfileSettingsView.as_view(), name="settings"),

    path("reset_password/",
         PasswordResetView.as_view(template_name="users/reset_password.html", form_class=CustomPasswordResetForm),
         name="reset_password"),
    path("reset_password/done/",
         PasswordResetDoneView.as_view(template_name="users/reset_password_done.html"),
         name="password_reset_done"),
    path("reset_password/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name="users/reset_password_confirm.html"),
         name="password_reset_confirm"),
    path("reset_password/complete/",
         PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"),
         name="password_reset_complete"),
    path("change_password/",
         PasswordChangeView.as_view(template_name="users/change_password_form.html"),
         name="password_change"),
    path("change_password/done/",
         PasswordChangeDoneView.as_view(template_name="users/change_password_done.html"),
         name="password_change_done")
]
