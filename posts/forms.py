from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    """Форма создания/редактирования поста"""

    class Meta:
        model = Post
        fields = ("content", "image",)
