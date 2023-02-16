from django import template

from users import forms


register = template.Library()


@register.inclusion_tag("users/tags/authentication_tag.html")
def show_forms():
    """Templatetag, отвечающий за передачу форм регистрации и аутентификации"""
    return {"register_form": forms.UserRegisterForm, "login_form": forms.UserLoginForm}
