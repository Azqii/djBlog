from django.urls import re_path

from .views import FollowView, UnfollowView

urlpatterns = [
    re_path(r"^profile/id(?P<follow_to_id>\d+)/follow/$", FollowView.as_view(), name="follow"),
    re_path(r"^profile/id(?P<unfollow_id>\d+)/unfollow/$", UnfollowView.as_view(), name="unfollow"),
]