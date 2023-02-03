from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy


class AuthorAccessMixin:
    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.user_id != self.request.user.id:
            raise PermissionDenied()
        return obj


class SuccessUrlMixin:
    def get_success_url(self):
        return reverse_lazy("post", kwargs={"post_id": self.kwargs["post_id"]})
