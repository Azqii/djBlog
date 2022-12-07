from django.urls import re_path

from .views import FollowView, UnfollowView

urlpatterns = [
    re_path(r"^follow/(?P<follow_to_id>\d+)/$", FollowView.as_view(), name="follow"),
    re_path(r"^unfollow/(?P<unfollow_id>\d+)/$", UnfollowView.as_view(), name="unfollow"),
]