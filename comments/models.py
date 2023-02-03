from django.conf import settings
from django.db import models

from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="comments"
    )
    content = models.TextField(verbose_name="Текст", max_length=1500, blank=False)
    time_created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    time_updated = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-time_created",)
