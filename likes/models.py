from django.conf import settings
from django.db import models

from posts.models import Post


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="likes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="likes"
    )
    time_created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    class Meta:
        unique_together = ("post", "user",)
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
