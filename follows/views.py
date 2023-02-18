from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from .services import get_follow_response, get_unfollow_response


class FollowView(LoginRequiredMixin, View):
    """View подписки с AJAX-запросом"""

    def post(self, request, *args, **kwargs):
        id_to_follow = int(request.POST.get("target"))

        response = get_follow_response(user=self.request.user, follow_id=id_to_follow)
        return JsonResponse(response)


class UnfollowView(LoginRequiredMixin, View):
    """View отписки с AJAX-запросом"""

    def post(self, request, *args, **kwargs):
        id_to_unfollow = int(request.POST.get("target"))

        response = get_unfollow_response(user=self.request.user, unfollow_id=id_to_unfollow)
        return JsonResponse(response)
