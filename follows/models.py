from django.conf import settings
from django.db import models


class Follow(models.Model):
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  verbose_name="Подписка на", related_name="followers")
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 verbose_name="Подписчик", related_name="follows")

    time_created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"follow id: {self.id} | {self.follower_id} follows {self.following_id}"

    def get_absolute_url(self):
        # TODO: Написать метод для absolute url подписок, если он нужен
        pass
