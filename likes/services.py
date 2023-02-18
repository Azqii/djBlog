from django.contrib.auth import get_user_model
from django.db import IntegrityError

from likes.repository import LikesRepository

User = get_user_model()


def get_like_response(user: User, post_id: int) -> dict:
    """Формирует ответ для клиента при постановке лайка посту с идентификатором post_id пользователем user"""
    try:
        LikesRepository.like_post(user=user, post_id=post_id)
    except IntegrityError:
        return {"succeed": False}
    return {"succeed": True, "likes": LikesRepository.get_likes_count_of_post(post_id=post_id)}


def get_unlike_response(user: User, post_id: int) -> dict:
    """Формирует ответ для клиента при снятии лайка с поста с идентификатором post_id пользователем user"""
    if not LikesRepository.post_exists(user=user, post_id=post_id):
        return {"succeed": False}
    LikesRepository.unlike_post(user=user, post_id=post_id)
    return {"succeed": True, "likes": LikesRepository.get_likes_count_of_post(post_id=post_id)}
