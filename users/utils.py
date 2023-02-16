from django.shortcuts import redirect


class AuthenticationErrorsMixin:
    """Миксин аутентификации"""
    template_name = "users/form_errors.html"
    extra_context = {"title": "Ошибка аутентификации"}

    def get(self, request, *args, **kwargs):
        """
        При запросе с методом GET перенаправляет на страницу аутентификации
        """
        return redirect("authentication")
