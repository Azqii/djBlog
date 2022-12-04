from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from users.models import Profile
from posts.models import Post


def index(request):
    if request.user.is_authenticated:
        return redirect("feed", permanent=True)
    return redirect("authentication", permanent=True)


class ProfileView(DetailView):
    queryset = Profile.objects.select_related("user")
    template_name = "blog/profile.html"
    pk_url_kwarg = "profile_id"
    context_object_name = "profile"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        page = self.request.GET.get("page")
        posts = Post.objects.filter(author_id=context["profile"].id).select_related("author__profile")
        context["posts"] = Paginator(posts, 6).get_page(page)
        context["title"] = context["profile"].user.username
        return context
