from django.conf import settings
from django.db import models


class Follow(models.Model):
    """Модель подписки одного пользователя на другого"""
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Подписка на", related_name="followers"
    )
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Подписчик", related_name="follows"
    )
    time_created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    class Meta:
        unique_together = ("following", "follower",)
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ("time_created",)
