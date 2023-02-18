from django.contrib.auth import get_user_model

from .repository import UserRepository, ProfileRepository

User = get_user_model()


def save_user_profile_info(user: User, info: dict) -> None:
    """Сохраняет информацию о юзере и его профиле."""
    UserRepository.update_name(user=user, first_name=info["first_name"], last_name=info["last_name"])
    ProfileRepository.update_info(
        profile=user.profile, photo=info["photo"], vk=info["vk"],
        tg=info["tg"], instagram=info["instagram"], bio=info["bio"]
    )
