from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Auth User model.

    Username, email and passwords are required.
    """

    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        verbose_name="Адрес эл. почты", unique=True,
        error_messages={"unique": "Пользователь с такой эл. почтой уже существует"},
    )
    username = models.CharField(
        verbose_name="Имя пользователя", unique=True, max_length=50, validators=[username_validator],
        error_messages={"unique": "Пользователь с таким именем уже существует"},
    )
    first_name = models.CharField(verbose_name="Имя", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, blank=True)
    is_staff = models.BooleanField(verbose_name="Сотрудник", default=False)
    is_active = models.BooleanField(verbose_name="Активный", default=True)
    date_joined = models.DateTimeField(verbose_name="Дата регистрации", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    """
    User's profile info model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Фото", upload_to="profile_pictures/", blank=True)
    vk = models.CharField(verbose_name="Профиль Вконтакте", max_length=100, blank=True)
    tg = models.CharField(verbose_name="Профиль Telegram", max_length=100, blank=True)
    instagram = models.CharField(verbose_name="Профиль Instagram", max_length=100, blank=True)
    bio = models.TextField(verbose_name="О себе", blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ("-user__date_joined",)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_id": self.id})


@receiver(post_save, sender=User)
def create_update_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
