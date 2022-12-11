from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from posts.models import Post
from users.models import Profile
from follows.models import Follow


def index(request):
    if request.user.is_authenticated:
        return redirect("feed", permanent=True)
    return redirect("authentication", permanent=True)


class PostView(DetailView):
    queryset = Post.objects.select_related("author__profile")
    template_name = "posts/post.html"
    pk_url_kwarg = "post_id"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Пост от {self.object.time_created.date()} | Автор: {self.object.author.username}"
        return context


class FeedPosts(LoginRequiredMixin, ListView):
    login_url = "authentication"
    model = Post
    template_name = "blog/feed.html"
    paginate_by = 6

    def get_queryset(self):
        sub_qs = Follow.objects.filter(follower=self.request.user.id).values_list("following_id", flat=True)
        return Post.objects.filter(author_id__in=sub_qs).select_related("author__profile")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости"
        return context


class ProfilePosts(SingleObjectMixin, ListView):
    template_name = "blog/profile.html"
    pk_url_kwarg = "profile_id"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(
            queryset=Profile.objects.select_related("user").prefetch_related("user__followers", "user__follows"))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.user.posts.select_related("author__profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.user.username
        if self.object.user.id != self.request.user.id:
            context["already_following"] = self.object.user.followers.filter(follower=self.request.user).exists()
        return context


class ProfileFollowsView(SingleObjectMixin, ListView):
    template_name = "blog/follows_list.html"
    pk_url_kwarg = "profile_id"
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Profile.objects.select_related("user"))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.user.follows.select_related("following__profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Подписки {self.object.user.username}"
        return context


class ProfileFollowersView(SingleObjectMixin, ListView):
    template_name = "blog/followers_list.html"
    pk_url_kwarg = "profile_id"
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Profile.objects.select_related("user"))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.user.followers.select_related("follower__profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Подписчики {self.object.user.username}"
        return context
