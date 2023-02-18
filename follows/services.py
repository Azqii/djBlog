from django.contrib.auth import get_user_model
from django.db import IntegrityError

from follows.repository import FollowsRepository

User = get_user_model()


def get_follow_response(user: User, follow_id: int) -> dict:
    """Формирует ответ для клиента при подписке пользователя user на пользователя с идентификатором follow_id"""
    if user.id == follow_id:
        return {"succeed": False}

    try:
        FollowsRepository.follow(follow_to_id=follow_id, user=user)
    except IntegrityError:
        return {"succeed": False}

    return {"succeed": True}


def get_unfollow_response(user: User, unfollow_id: int) -> dict:
    """Формирует ответ для клиента при отписке пользователя user от пользователя с идентификатором unfollow_id"""
    if user.id == unfollow_id:
        return {"succeed": False}

    if not FollowsRepository.follow_exists(following_id=unfollow_id, follower=user):
        return {"succeed": False}

    FollowsRepository.unfollow(unfollow_id=unfollow_id, user=user)
    return {"succeed": True}
