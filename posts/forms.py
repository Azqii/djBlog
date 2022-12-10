from django import forms
from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("content", "image",)
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0",
                "placeholder": "Содержание поста"}),
            "image": forms.FileInput(attrs={
                "class": "form-control bg-transparent rounded-0 border-bottom shadow-none pb-15 px-0"}),
        }
        labels = {
            "content": "Содержание",
            "image": "Изображение",
        }
