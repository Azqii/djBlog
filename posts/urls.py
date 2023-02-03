from django.urls import path

from .views import AddPostView, EditPostView, DeletePostView


urlpatterns = [
    path("post/add/", AddPostView.as_view(), name="add_post"),
    path("post/<int:post_id>/edit/", EditPostView.as_view(), name="edit_post"),
    path("post/<int:post_id>/delete/", DeletePostView.as_view(), name="delete_post"),
]
