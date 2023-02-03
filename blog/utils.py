from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from users.models import Profile

class BaseProfileFollowsView(SingleObjectMixin, ListView):
    pk_url_kwarg = "profile_id"
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Profile.objects.select_related("user"))
        return super().get(request, *args, **kwargs)
