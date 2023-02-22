from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .utils import AuthorAccessMixin


class AddPostView(LoginRequiredMixin, CreateView):
    """View создания поста"""
    form_class = PostForm
    template_name = "posts/post_form.html"
    extra_context = {"title": "Новый пост"}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(AuthorAccessMixin, UpdateView):
    """View редактирования поста"""
    model = Post
    form_class = PostForm
    pk_url_kwarg = "post_id"
    template_name = "posts/post_form.html"
    extra_context = {"title": "Редактировать пост"}


class DeletePostView(AuthorAccessMixin, DeleteView):
    """View удаления поста"""
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "posts/post_confirm_delete.html"
    extra_context = {"title": "Удалить пост"}

    def get_success_url(self):
        return reverse("profile", kwargs={"profile_id": self.request.user.profile.id})
