from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.core.cache import cache

from apps.friends.models import Relationship
from apps.profiles.models import Profile


User = get_user_model()


@receiver(
    post_save, sender=Relationship, dispatch_uid="relationship_relationship_updated"
)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == "accepted":
        print(sender_.user)
        print(receiver_.user)
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()

    paginator = Paginator(Relationship.objects.all(), 30)
    num = paginator.num_pages
    for page in range(1, num + 1):
        cache.delete(f"list_relation_receiver_and_sender_context_{page}")


@receiver(
    pre_delete, sender=Relationship, dispatch_uid="relationship_relationship_deleted"
)
def pre_delete_remove_from_friend(sender, instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    sender.friends.remove(receiver.user)
    receiver.friends.remove(sender.user)
    sender.save()
    receiver.save()

    paginator = Paginator(Relationship.objects.all(), 30)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"list_relation_receiver_and_sender_context_{page}")


@receiver(post_save, sender=User, dispatch_uid="relationship_user_updated")
def user_updated(sender, instance, **kwargs) -> None:
    paginator = Paginator(Relationship.objects.all(), 30)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"list_relation_receiver_and_sender_context_{page}")


@receiver(pre_delete, sender=User, dispatch_uid="relationship_user_deleted")
def user_deleted(sender, instance, **kwargs) -> None:
    paginator = Paginator(Relationship.objects.all(), 30)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"list_relation_receiver_and_sender_context_{page}")


@receiver(post_save, sender=Profile, dispatch_uid="relationship_profile_updated")
def profile_updated(sender, instance, **kwargs) -> None:
    paginator = Paginator(Relationship.objects.all(), 30)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"list_relation_receiver_and_sender_context_{page}")


@receiver(pre_delete, sender=Profile, dispatch_uid="relationship_profile_deleted")
def profile_deleted(sender, instance, **kwargs) -> None:
    paginator = Paginator(Relationship.objects.all(), 30)
    num = paginator.num_pages
    for page in range(1, num + 2):
        cache.delete(f"list_relation_receiver_and_sender_context_{page}")
