from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from .models import Like


class LikeView(LoginRequiredMixin, View):
    login_url = "authentication"

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")

        try:
            Like.objects.create(user_id=self.request.user.id, post_id=post_id)
        except IntegrityError:
            print(f"{post_id} error")

        return redirect("post", post_id)  # TODO: переписать с AJAX


class UnlikeView(LoginRequiredMixin, View):
    login_url = "authentication"

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")

        Like.objects.filter(user_id=self.request.user.id, post_id=post_id).delete()

        return redirect("post", post_id)  # TODO: переписать с AJAX
