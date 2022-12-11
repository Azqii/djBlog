from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from .models import Follow


class FollowView(LoginRequiredMixin, View):
    login_url = "authentication"

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
    login_url = "authentication"

    def post(self, request, *args, **kwargs):
        id_to_unfollow = request.POST.get("id_to_unfollow")
        record = Follow.objects.filter(following=id_to_unfollow, follower=self.request.user.id)

        if record:
            record.delete()
        else:
            pass
        return redirect("profile", id_to_unfollow) # TODO: переписать с AJAX