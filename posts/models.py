from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Модель поста пользователя"""
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор", related_name="posts"
    )
    image = models.ImageField(verbose_name="Картинка", upload_to="post_pictures/", blank=True)
    content = models.TextField(verbose_name="Текст", max_length=2000, blank=False)
    time_created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    time_updated = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("-time_created",)

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.id})
