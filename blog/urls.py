from django.urls import path

from .views import index_view, ProfilePostsView, FeedPostsView, PostView, ProfileFollowsView, ProfileFollowersView, \
    UsersSearchView

urlpatterns = [
    path("", index_view, name="index"),
    path("post/<int:post_id>/", PostView.as_view(), name="post"),
    path("feed/", FeedPostsView.as_view(), name="feed"),
    path("profile/id<int:profile_id>/", ProfilePostsView.as_view(), name="profile"),
    path("profile/id<int:profile_id>/follows/", ProfileFollowsView.as_view(), name="follows"),
    path("profile/id<int:profile_id>/followers/", ProfileFollowersView.as_view(), name="followers"),
    path("search/", UsersSearchView.as_view(), name="user_search"),
]
