from django.contrib.auth import get_user_model
from django.db.models import QuerySet, Exists, Count, Value, Q
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
    def get_profile_with_user_and_following_info(profile_id: int, user: User) -> QuerySet:
        """
        Возвращает QuerySet профиля с полями пользователя и информацией о подписке
        пользователя user на другого пользователя с id profile_id
        """
        sub_qs = Exists(Follow.objects.filter(following_id=profile_id, follower_id=user.id))
        return BlogRepository.get_profile_with_user().annotate(already_following=sub_qs)

    @staticmethod
    def get_post_with_profile_comments_and_likes_info(post_id: int, user: User) -> QuerySet:
        sub_qs = Exists(Like.objects.filter(post_id=post_id, user_id=user.id))
        return Post.objects.\
            select_related("author__profile").\
            prefetch_related("comments__user__profile").\
            annotate(already_liked=sub_qs, likes_count=Count("likes"))

    @staticmethod
    def get_posts_of_follows_with_profiles(user: User) -> QuerySet:
        sub_qs = Follow.objects.filter(follower=user.id).values_list("following_id", flat=True)
        return Post.objects.filter(author_id__in=sub_qs).select_related("author__profile")

    @staticmethod
    def get_posts_of_profile(profile: Profile) -> QuerySet:
        return profile.user.posts.select_related("author__profile")

    @staticmethod
    def get_follows_of_profile(profile: Profile) -> QuerySet:
        return profile.user.follows.select_related("following__profile")

    @staticmethod
    def get_followers_of_profile(profile: Profile) -> QuerySet:
        return profile.user.followers.select_related("follower__profile")

    @staticmethod
    def get_profiles_with_name(name: str):
        return Profile.objects.\
            select_related("user").\
            annotate(full_name=Concat("user__first_name", Value(" "), "user__last_name")).\
            filter(Q(user__username__icontains=name) | Q(full_name__icontains=name))
