from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from .repository import BlogRepository


class BaseProfileFollowsView(SingleObjectMixin, ListView):
    """Базовое View подписок/подписчиков пользователя"""
    pk_url_kwarg = "profile_id"
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=BlogRepository.get_profile_with_user())
        return super().get(request, *args, **kwargs)
