from django.core.exceptions import PermissionDenied


class AuthorAccessMixin:
    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author_id != self.request.user.id:
            raise PermissionDenied()
        return obj