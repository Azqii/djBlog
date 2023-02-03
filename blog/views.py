from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef, Count, Q, Value
from django.db.models.functions import Concat
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from posts.models import Post
from users.models import Profile
from follows.models import Follow
from likes.models import Like
from .utils import BaseProfileFollowsView


def index(request):
    if request.user.is_authenticated:
        return redirect("feed", permanent=True)
    return redirect("authentication", permanent=True)


class PostView(DetailView):
    template_name = "blog/post.html"
    pk_url_kwarg = "post_id"
    context_object_name = "post"

    def get_queryset(self):
        sub_qs = Exists(Like.objects.filter(post_id=OuterRef("pk"), user_id=self.request.user.id))
        return Post.objects.select_related(
            "author__profile").prefetch_related(
            "comments__user__profile").annotate(
            already_liked=sub_qs, likes_count=Count("likes")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Пост от {self.object.time_created.date()} | Автор: {self.object.author.username}"
        return context


class FeedPostsView(LoginRequiredMixin, ListView):
    template_name = "blog/feed.html"
    extra_context = {"title": "Новости"}
    paginate_by = 6

    def get_queryset(self):
        sub_qs = Follow.objects.filter(follower=self.request.user.id).values_list("following_id", flat=True)
        return Post.objects.filter(author_id__in=sub_qs).select_related("author__profile")


class ProfilePostsView(SingleObjectMixin, ListView):
    template_name = "blog/profile.html"
    pk_url_kwarg = "profile_id"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        sub_qs = Exists(Follow.objects.filter(following_id=OuterRef("pk"), follower_id=self.request.user.id))
        self.object = self.get_object(
            queryset=Profile.objects.select_related("user").annotate(already_following=sub_qs)
        )
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.user.posts.select_related("author__profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.user.username
        return context


class ProfileFollowsView(BaseProfileFollowsView):
    template_name = "blog/follows_list.html"

    def get_queryset(self):
        return self.object.user.follows.select_related("following__profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Подписки {self.object.user.username}"
        return context


class ProfileFollowersView(BaseProfileFollowsView):
    template_name = "blog/followers_list.html"

    def get_queryset(self):
        return self.object.user.followers.select_related("follower__profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Подписчики {self.object.user.username}"
        return context


class UsersSearchView(ListView):
    template_name = "blog/profiles_list.html"
    extra_context = {"title": "Поиск"}
    paginate_by = 8

    def get_queryset(self):
        search_query = self.request.GET.get("name", "")
        return Profile.objects.select_related("user").annotate(
            full_name=Concat("user__first_name", Value(" "), "user__last_name")).filter(
            Q(user__username__icontains=search_query) | Q(full_name__icontains=search_query)
        )
