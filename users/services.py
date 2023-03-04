from django.contrib.auth import get_user_model
from django.db import transaction

from .repository import UserRepository, ProfileRepository

User = get_user_model()


def save_user_profile_info(user: User, info: dict) -> None:
    """Сохраняет информацию о юзере и его профиле."""
    with transaction.atomic():
        UserRepository.update_name(user=user, first_name=info["first_name"], last_name=info["last_name"])
        ProfileRepository.update_info(
            profile=user.profile, photo=info["photo"], vk=info["vk"],
            tg=info["tg"], instagram=info["instagram"], bio=info["bio"]
        )


def get_user_info(user: User) -> dict:
    """Возвращает информацию о пользователе user, в которую входит его имя, описание, фото и профили в соц. сетях"""
    info = {
        "first_name": user.first_name, "last_name": user.last_name,
        "vk": user.profile.vk, "tg": user.profile.tg,
        "instagram": user.profile.instagram, "bio": user.profile.bio,
        "photo": user.profile.photo
    }
    return info
