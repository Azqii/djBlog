from django.urls import path

from .views import AddPost, EditPost, DeletePost


urlpatterns = [
    path("post/add/", AddPost.as_view(), name="add_post"),
    path("post/<int:post_id>/edit/", EditPost.as_view(), name="edit_post"),
    path("post/<int:post_id>/delete/", DeletePost.as_view(), name="delete_post"),
]
