from django.contrib.auth import get_user_model

from .models import Like

User = get_user_model()


class LikesRepository:
    @staticmethod
    def like_post(user: User, post_id: int) -> None:
        """Лайк на пост с id post_id от пользователя user"""
        Like.objects.create(user_id=user.id, post_id=post_id)

    @staticmethod
    def unlike_post(user:User, post_id:int) -> None:
        """Снятие лайка с поста с id post_id от пользователя user"""
        Like.objects.filter(user_id=user.id, post_id=post_id).delete()