from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views import View

from .repository import LikesRepository


class LikeView(LoginRequiredMixin, View):
    """View добавления лайка"""
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")

        try:
            LikesRepository.like_post(user=self.request.user, post_id=post_id)
        except IntegrityError:
            pass
        return redirect("post", post_id)  # TODO: переписать с AJAX


class UnlikeView(LoginRequiredMixin, View):
    """View удаления лайка"""
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")

        LikesRepository.unlike_post(user=self.request.user, post_id=post_id)
        return redirect("post", post_id)  # TODO: переписать с AJAX
