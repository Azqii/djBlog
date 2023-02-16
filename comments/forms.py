from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    """Форма написания комментария"""
    class Meta:
        model = Comment
        fields = ("content",)
