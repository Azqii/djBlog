from django.conf import settings
from django.db import models

from posts.models import Post


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             verbose_name="Пост", related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name="Пользователь", related_name="likes")
    time_created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

    def __str__(self):
        return f"post like id: {self.id}"

    def get_absolute_url(self):
        # TODO: Написать метод для absolute url лайка постов, если он нужен
        pass
