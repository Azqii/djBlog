from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from .utils import BaseProfileFollowsView
from .repository import BlogRepository


def index_view(request):
    """View для переадресации с '/'"""
    if request.user.is_authenticated:
        return redirect("feed", permanent=True)
    return redirect("authentication", permanent=True)


class PostView(DetailView):
    """View отдельного поста"""
    template_name = "blog/post.html"
    pk_url_kwarg = "post_id"
    context_object_name = "post"

    def get_queryset(self):
        return BlogRepository.get_post_with_profile_comments_and_likes_info(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Пост от {self.object.time_created.date()} | Автор: {self.object.author.username}"
        return context


class FeedPostsView(LoginRequiredMixin, ListView):
    """View списка постов в разделе новостей"""
    template_name = "blog/feed.html"
    extra_context = {"title": "Новости"}
    paginate_by = 6

    def get_queryset(self):
        return BlogRepository.get_posts_of_follows_with_profiles_and_likes_info(user=self.request.user)


class ProfilePostsView(SingleObjectMixin, ListView):
    """View списка постов в профиле пользователя"""
    template_name = "blog/profile.html"
    pk_url_kwarg = "profile_id"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(
            BlogRepository.get_profile_with_user_and_following_info(user=request.user)
        )
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return BlogRepository.get_posts_of_profile_with_likes_info(user=self.request.user, profile=self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.user.username
        return context


class ProfileFollowsView(BaseProfileFollowsView):
    """View списка подписок пользователя"""
    template_name = "blog/profiles_list.html"

    def get_queryset(self):
        return BlogRepository.get_follows_of_profile(user=self.request.user, profile=self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Подписки {self.object.user.username}"
        return context


class ProfileFollowersView(BaseProfileFollowsView):
    """View списка подписчиков пользователя"""
    template_name = "blog/profiles_list.html"

    def get_queryset(self):
        return BlogRepository.get_followers_of_profile(user=self.request.user, profile=self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Подписчики {self.object.user.username}"
        return context


class UsersSearchView(ListView):
    """View поиска пользователей"""
    template_name = "blog/profiles_list.html"
    extra_context = {"title": "Поиск"}
    paginate_by = 8

    def get_queryset(self):
        name = self.request.GET.get("name", "")
        return BlogRepository.get_profiles_with_names_and_following_info(user=self.request.user, name=name)
