from .models import Profile, User


class UserRepository:
    @staticmethod
    def update_name(user: User, first_name: str, last_name: str) -> None:
        """Обновление имени first_name и фамилии last_name пользователя user"""
        User.objects.filter(id=user.id).update(first_name=first_name, last_name=last_name)


class ProfileRepository:
    @staticmethod
    def update_info(profile: Profile, photo, vk: str, tg: str, instagram: str, bio: str) -> None:
        """Обновление информации профиля profile соответствующими полями"""
        profile.photo = photo
        profile.vk = vk
        profile.tg = tg
        profile.instagram = instagram
        profile.bio = bio
        profile.save()
