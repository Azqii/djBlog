from django import template

from users import forms


register = template.Library()


@register.inclusion_tag("users/authentication_tag.html")
def show_forms():
    return {"register_form": forms.UserRegisterForm, "login_form": forms.UserLoginForm}
