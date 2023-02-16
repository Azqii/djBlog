from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views import View

from .repository import FollowsRepository


class FollowView(LoginRequiredMixin, View):
    """View подписки"""
    def post(self, request, *args, **kwargs):
        id_to_follow = request.POST.get("id_to_follow")

        if self.request.user.id == int(id_to_follow):
            return redirect("profile", self.request.user.id)

        try:
            FollowsRepository.follow(follow_to_id=id_to_follow, user=self.request.user)
        except IntegrityError:
            pass
        return redirect("profile", id_to_follow)  # TODO: переписать с AJAX


class UnfollowView(LoginRequiredMixin, View):
    """View отписки"""
    def post(self, request, *args, **kwargs):
        id_to_unfollow = request.POST.get("id_to_unfollow")

        if self.request.user.id == int(id_to_unfollow):
            return redirect("profile", self.request.user.id)

        FollowsRepository.unfollow(unfollow_id=id_to_unfollow, user=self.request.user)
        return redirect("profile", id_to_unfollow)  # TODO: переписать с AJAX
