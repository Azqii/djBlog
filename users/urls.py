from django.urls import path

from .views import UserRegister, UserLogin, logout_user, UserAuthentication

urlpatterns = [
    path("authentication/", UserAuthentication.as_view(), name="authentication"),
    path("register/", UserRegister.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
]
