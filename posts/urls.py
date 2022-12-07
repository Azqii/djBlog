from django.urls import path

from .views import Feed, ProfilePosts

urlpatterns = [
    path("feed/", Feed.as_view(), name="feed"),
    path("profile/id<int:profile_id>/", ProfilePosts.as_view(), name="profile"),
]
