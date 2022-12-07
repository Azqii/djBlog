from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post
from users.models import Profile
from follows.models import Follow


class ProfilePosts(DetailView):
    queryset = Profile.objects.select_related("user")
    template_name = "posts/profile.html"
    pk_url_kwarg = "profile_id"
    context_object_name = "profile"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProfilePosts, self).get_context_data(**kwargs)
        page = self.request.GET.get("page")
        posts = Post.objects.filter(author_id=self.object.user.id).select_related("author__profile")
        context["posts"] = Paginator(posts, 6).get_page(page)
        context["already_following"] = self.object.user.followers.filter(follower=self.request.user).exists()
        context["title"] = context["profile"].user.username
        return context


class Feed(ListView):
    model = Post
    template_name = "posts/feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        sub_qs = Follow.objects.filter(follower=self.request.user.id).values_list("following_id", flat=True)
        return Post.objects.filter(author_id__in=sub_qs).select_related("author__profile")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости"
        return context


def feed(request):
    # TODO: переписать
    return render(request, "base.html", context={"title": "Новости"})
