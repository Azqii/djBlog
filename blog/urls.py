from django.urls import path

from .views import index, ProfilePosts, FeedPosts


urlpatterns = [
    path("", index, name="index"),
    path("feed/", FeedPosts.as_view(), name="feed"),
    path("profile/id<int:profile_id>/", ProfilePosts.as_view(), name="profile"),
]
