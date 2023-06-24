import os
import uuid
import cloudinary
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.paginator import Paginator
from django.core.cache import cache

from apps.comments.models import Comment
from apps.post.models import Post
from apps.profiles.models import Profile
from config.settings import ENV


@receiver(post_save, sender=Post, dispatch_uid="post_posts_updated")
def save_uid_post(sender, instance, **kwargs) -> None:
    if instance.uid == "":
        instance.uid = (
            str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(uuid.uuid4()).replace("-", "")
            + str(instance.id)
        )
        instance.save()
    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 1):
        cache.delete(f"posts_list_{page}")


@receiver(pre_delete, sender=Post, dispatch_uid="post_post_deleted")
def image_delete(sender, instance, **kwargs) -> None:
    if ENV == "production":
        if instance.img:
            cloudinary.uploader.destroy(str(instance.img))
    else:
        if instance.img:
            try:
                os.remove(instance.img.path)
            except Exception:
                cloudinary.uploader.destroy(str(instance.img))

    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"posts_list_{page}")


@receiver(post_save, sender=Comment, dispatch_uid="post_comments_updated")
def comments_updated(sender, instance, **kwargs) -> None:
    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 1):
        cache.delete(f"posts_list_{page}")


@receiver(pre_delete, sender=Comment, dispatch_uid="post_comments_deleted")
def comments_deleted(sender, instance, **kwargs) -> None:
    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"posts_list_{page}")


@receiver(post_save, sender=get_user_model(), dispatch_uid="post_user_updated")
def user_updated(sender, instance, **kwargs) -> None:
    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 1):
        cache.delete(f"posts_list_{page}")


@receiver(pre_delete, sender=get_user_model(), dispatch_uid="post_user_deleted")
def user_deleted(sender, instance, **kwargs) -> None:
    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"posts_list_{page}")


@receiver(post_save, sender=Profile, dispatch_uid="post_profile_updated")
def profile_updated(sender, instance, **kwargs) -> None:
    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 1):
        cache.delete(f"posts_list_{page}")


@receiver(pre_delete, sender=Profile, dispatch_uid="post_profile_deleted")
def profile_deleted(sender, instance, **kwargs) -> None:
    paginator = Paginator(Post.objects.all(), 6)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"posts_list_{page}")
