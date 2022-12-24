from django import forms
from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0"})
        }
        labels = {
            "content": "Комментарий",
        }
