from django.urls import path

from .views import AddCommentView, DeleteCommentView, EditCommentView

urlpatterns = [
    path("post/<int:post_id>/comment/add/", AddCommentView.as_view(), name="add_comment"),
    path("post/<int:post_id>/comment/<int:comment_id>/edit/", EditCommentView.as_view(), name="edit_comment"),
    path("post/<int:post_id>/comment/<int:comment_id>/delete/", DeleteCommentView.as_view(), name="delete_comment"),
]