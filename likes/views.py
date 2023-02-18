from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from .services import get_like_response, get_unlike_response


class LikeView(LoginRequiredMixin, View):
    """View добавления лайка AJAX-запросом"""

    def post(self, request, *args, **kwargs):
        post_id = int(request.POST.get("post_id"))

        response = get_like_response(user=self.request.user, post_id=post_id)
        return JsonResponse(response)


class UnlikeView(LoginRequiredMixin, View):
    """View удаления лайка AJAX-запросом"""

    def post(self, request, *args, **kwargs):
        post_id = int(request.POST.get("post_id"))

        response = get_unlike_response(user=self.request.user, post_id=post_id)
        return JsonResponse(response)
