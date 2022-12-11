from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post


class AddPost(LoginRequiredMixin, CreateView):
    login_url = "authentication"
    form_class = PostForm
    template_name = "posts/post_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новый пост"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    pk_url_kwarg = "post_id"
    template_name = "posts/post_form.html"

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author_id != self.request.user.id:
            raise PermissionDenied()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать пост"
        return context


class DeletePost(DeleteView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "posts/post_confirm_delete.html"

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author_id != self.request.user.id:
            raise PermissionDenied()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удалить пост"
        return context

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"profile_id": self.request.user.profile.id})
