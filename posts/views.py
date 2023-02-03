from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .utils import AuthorAccessMixin


class AddPostView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "posts/post_form.html"
    extra_context = {"title": "Новый пост"}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(AuthorAccessMixin, UpdateView):
    model = Post
    form_class = PostForm
    pk_url_kwarg = "post_id"
    template_name = "posts/post_form.html"
    extra_context = {"title": "Редактировать пост"}


class DeletePostView(AuthorAccessMixin, DeleteView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "posts/post_confirm_delete.html"
    extra_context = {"title": "Удалить пост"}

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"profile_id": self.request.user.profile.id})
