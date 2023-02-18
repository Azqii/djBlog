from django.contrib.auth import get_user_model

from follows.models import Follow

User = get_user_model()


class FollowsRepository:
    @staticmethod
    def follow(follow_to_id: int, user: User) -> None:
        """Подписка на пользователя с id follow_to_id пользователем user"""
        Follow.objects.create(following_id=follow_to_id, follower_id=user.id)

    @staticmethod
    def follow_exists(following_id: int, follower: User) -> bool:
        """
        Возвращает True или False в зависимости от того, подписан ли пользователь follower на пользователя
        с идентификатором following_id
        """
        return Follow.objects.filter(following_id=following_id, follower_id=follower.id).exists()

    @staticmethod
    def unfollow(unfollow_id: int, user: User) -> None:
        """Отписка от пользователя с id unfollow_id пользователем user"""
        Follow.objects.filter(following_id=unfollow_id, follower_id=user.id).delete()
