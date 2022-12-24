from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import CommentForm
from .models import Comment


class AddCommentView(LoginRequiredMixin, CreateView):
    login_url = "authentication"
    form_class = CommentForm
    template_name = "comments/comment_form.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.post_id = self.kwargs["post_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post", kwargs={"post_id": self.kwargs["post_id"]})


class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    pk_url_kwarg = "comment_id"
    template_name = "comments/comment_form.html"

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.user_id != self.request.user.id:
            raise PermissionDenied()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать комментарий"
        return context

    def get_success_url(self):
        return reverse_lazy("post", kwargs={"post_id": self.kwargs["post_id"]})


class DeleteCommentView(DeleteView):
    model = Comment
    pk_url_kwarg = "comment_id"
    template_name = "comments/comment_confirm_delete.html"

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.user_id != self.request.user.id:
            raise PermissionDenied()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удалить комментарий"
        return context

    def get_success_url(self):
        return reverse_lazy("post", kwargs={"post_id": self.kwargs["post_id"]})
