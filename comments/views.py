from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import CommentForm
from .models import Comment
from .utils import AuthorAccessMixin, SuccessUrlMixin


class AddCommentView(LoginRequiredMixin, SuccessUrlMixin, CreateView):
    """View добавления комментария"""
    form_class = CommentForm
    template_name = "comments/comment_form.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.post_id = self.kwargs["post_id"]
        return super().form_valid(form)


class EditCommentView(AuthorAccessMixin, SuccessUrlMixin, UpdateView):
    """View редактирования комментария"""
    model = Comment
    form_class = CommentForm
    pk_url_kwarg = "comment_id"
    template_name = "comments/comment_form.html"
    extra_context = {"title": "Редактирование комментария"}


class DeleteCommentView(AuthorAccessMixin, SuccessUrlMixin, DeleteView):
    """View удаления комментария"""
    model = Comment
    pk_url_kwarg = "comment_id"
    template_name = "comments/comment_confirm_delete.html"
    extra_context = {"title": "Подтвердите удаление комментария"}
