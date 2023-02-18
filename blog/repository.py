from django.contrib.auth import get_user_model
from django.db.models import QuerySet, Exists, Count, Value, Q, OuterRef
from django.db.models.functions import Concat

from follows.models import Follow
from likes.models import Like
from posts.models import Post
from users.models import Profile

User = get_user_model()


class BlogRepository:
    @staticmethod
    def get_profile_with_user() -> QuerySet:
        """Возвращает QuerySet профиля с пользовательскими полями"""
        return Profile.objects.select_related("user")

    @staticmethod
    def get_profile_with_user_and_following_info(user: User) -> QuerySet:
        """
        Возвращает QuerySet профиля с полями пользователя и информацией о подписке
        пользователя user на другого пользователя с идентификатором profile_id
        """
        sub_qs = Exists(Follow.objects.filter(following_id=OuterRef("pk"), follower_id=user.id))
        return BlogRepository.get_profile_with_user().annotate(already_following=sub_qs)

    @staticmethod
    def get_posts_with_profiles_likes_info(user: User) -> QuerySet:
        """
        Возвращает QuerySet постов с информацией о профиле автора, количестве лайков и наличии лайка пользователя user
        """
        sub_qs = Exists(Like.objects.filter(post_id=OuterRef("pk"), user_id=user.id))
        return Post.objects. \
            select_related("author__profile"). \
            annotate(already_liked=sub_qs, likes_count=Count("likes")). \
            order_by("-time_created")

    @staticmethod
    def get_post_with_profile_comments_and_likes_info(user: User) -> QuerySet:
        """
        Возвращает QuerySet поста с идентификатором post_id с информацией о его авторе, лайках и комментариями
        """
        return BlogRepository.get_posts_with_profiles_likes_info(user=user).prefetch_related("comments__user__profile")

    @staticmethod
    def get_posts_of_follows_with_profiles_and_likes_info(user: User) -> QuerySet:
        """
        Возвращает QuerySet постов пользователей, на которых подписан user с информацией об их авторах и лайках
        """
        sub_qs = Follow.objects.filter(follower_id=user.id).values_list("following_id", flat=True)
        return BlogRepository.get_posts_with_profiles_likes_info(user).filter(author_id__in=sub_qs)

    @staticmethod
    def get_posts_of_profile_with_likes_info(user: User, profile: Profile) -> QuerySet:
        """Возвращает QuerySet постов пользователя с профилем profile с информацией об авторе и лайках"""
        return BlogRepository.get_posts_with_profiles_likes_info(user).filter(author=profile.user)

    @staticmethod
    def get_follows_of_profile(user: User, profile: Profile) -> QuerySet:
        """
        Возвращает QuerySet подписок пользователя с профилем profile и информацией о подписке на них
        пользователя user
        """
        sub_qs = Follow.objects.filter(follower_id=profile.user.id).values_list("following_id", flat=True)
        return BlogRepository.get_profile_with_user_and_following_info(user=user).filter(user_id__in=sub_qs)

    @staticmethod
    def get_followers_of_profile(user: User, profile: Profile) -> QuerySet:
        """
        Возвращает QuerySet подписчиков пользователя с профилем profile и информацией о подписке на них
        пользователя user
        """
        sub_qs = Follow.objects.filter(following_id=profile.user.id).values_list("follower_id", flat=True)
        return BlogRepository.get_profile_with_user_and_following_info(user=user).filter(user__id__in=sub_qs)

    @staticmethod
    def get_profiles_with_names_and_following_info(user: User, name: str) -> QuerySet:
        """
        Возвращает QuerySet профилей с информацией о подписке на них пользователя user,
        в которых в имени и фамилии или в имени пользователя есть совпадение с name
        """
        return BlogRepository.get_profile_with_user_and_following_info(user=user). \
            annotate(full_name=Concat("user__first_name", Value(" "), "user__last_name")). \
            filter(Q(user__username__icontains=name) | Q(full_name__icontains=name))
