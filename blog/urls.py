from django.urls import path

from .views import index, ProfileView

urlpatterns = [
    path("", index, name="index"),
    path("profile/id<int:profile_id>/", ProfileView.as_view(), name="profile")
]
