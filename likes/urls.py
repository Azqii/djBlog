from django.urls import path

from .views import LikeView, UnlikeView#, TestLike

urlpatterns = [
    path("post/like/", LikeView.as_view(), name="like"),
    path("post/unlike/", UnlikeView.as_view(), name="unlike"),
]
