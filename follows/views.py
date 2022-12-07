from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from .models import Follow


class FollowView(LoginRequiredMixin, View):
    login_url = "authentication"

    def get(self, request, follow_to_id, *args, **kwargs):
        if self.request.user.id == int(follow_to_id):
            return redirect("profile", self.request.user.id)
        try:
            Follow.objects.create(following_id=follow_to_id, follower_id=self.request.user.id)
        except IntegrityError:
            pass
        return redirect("profile", follow_to_id)  # TODO: переписать с AJAX


class UnfollowView(LoginRequiredMixin, View):
    login_url = "authentication"

    def get(self, request, unfollow_id, *args, **kwargs):
        record = Follow.objects.filter(following=unfollow_id, follower=self.request.user.id)
        if record:
            record.delete()
        else:
            pass
        return redirect("profile", unfollow_id)  # TODO: переписать с AJAX