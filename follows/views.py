from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views import View

from .models import Follow


class FollowView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        id_to_follow = request.POST.get("id_to_follow")

        if self.request.user.id == int(id_to_follow):
            return redirect("profile", self.request.user.id)

        try:
            Follow.objects.create(following_id=id_to_follow, follower_id=self.request.user.id)
        except IntegrityError:
            pass

        return redirect("profile", id_to_follow)  # TODO: переписать с AJAX


class UnfollowView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        id_to_unfollow = request.POST.get("id_to_unfollow")

        if self.request.user.id == int(id_to_unfollow):
            return redirect("profile", self.request.user.id)

        Follow.objects.filter(following_id=id_to_unfollow, follower_id=self.request.user.id).delete()

        return redirect("profile", id_to_unfollow)  # TODO: переписать с AJAX
