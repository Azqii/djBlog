from django.contrib.auth import get_user_model
from django.db.models import Count

from .models import Like
from posts.models import Post

User = get_user_model()


class LikesRepository:
    @staticmethod
    def like_post(user: User, post_id: int) -> None:
        """Лайк на пост с id post_id от пользователя user"""
        Like.objects.create(user_id=user.id, post_id=post_id)

    @staticmethod
    def post_exists(user: User, post_id: int) -> bool:
        """
        Возвращает True или False в зависимости от того, существует ли лайк от пользователя User на посте
        с идентификатором post_id
        """
        return Like.objects.filter(user_id=user.id, post_id=post_id).exists()

    @staticmethod
    def unlike_post(user: User, post_id: int) -> None:
        """Снятие лайка с поста с id post_id от пользователя user"""
        Like.objects.filter(user_id=user.id, post_id=post_id).delete()

    @staticmethod
    def get_likes_count_of_post(post_id: int) -> int:
        """Возвращает количество лайков на посте с идентификатором post_id"""
        return Post.objects.annotate(likes_count=Count("likes")).values_list("likes_count", flat=True).get(pk=post_id)
