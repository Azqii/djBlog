from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm

from .models import User
from .tasks import send_reset_password_email


class UserRegisterForm(UserCreationForm):
    """Форма регистрации"""

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2",)


class UserLoginForm(AuthenticationForm):
    """Форма аутентификация"""
    username = forms.EmailField()


class CustomPasswordResetForm(PasswordResetForm):
    """Кастоманая форма сброса пароля для отправки писем с Celery"""

    def send_mail(self, subject_template_name, email_template_name, context,
                  from_email, to_email, html_email_template_name=None, ):
        context['user'] = context['user'].id
        send_reset_password_email.delay(
            subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name
        )


class ProfileSettingsForm(forms.Form):
    """
    Форма для настроек информации в профиле пользователя.

    Объединены некоторые поля из моделей User и Profile
    """
    photo = forms.ImageField(required=False)
    first_name = forms.CharField(required=False, max_length=150)
    last_name = forms.CharField(required=False, max_length=150)
    vk = forms.CharField(required=False, max_length=100)
    tg = forms.CharField(required=False, max_length=100)
    instagram = forms.CharField(required=False, max_length=100)
    bio = forms.CharField(required=False, widget=forms.Textarea())
