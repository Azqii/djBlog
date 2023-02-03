from django.shortcuts import redirect


class AuthenticationMixin:
    template_name = "users/form_errors.html"
    extra_context = {"title": "Ошибка аутентификации"}

    def get(self, request, *args, **kwargs):
        return redirect("authentication")
