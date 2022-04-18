from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
from apps.friends.models import Relationship
from apps.notifications.models import Notification
from apps.post.models import LikePost
from apps.comments.models import Comment


@receiver(post_save, sender=LikePost)
def post_save_add_notif_like_post(sender, instance, created, **kwargs):
    from_user = instance.user
    to_user = instance.post.author
    if instance.value == 'Like':
        if from_user != to_user:
            Notification.objects.create(
                type_notif='Like_Post',
                from_user=from_user,
                to_user=to_user,
                post=instance.post,
                like_post = instance
            )
    else:
        if Notification.objects.filter(like_post=instance).exists():
            notif = Notification.objects.get(like_post=instance)
            notif.delete()

@receiver(post_save, sender=Comment)
def post_save_add_notif_comment_post(sender, instance, created, **kwargs):
    from_user = instance.author
    to_user = instance.post.author
    if created:
        if from_user != to_user:
            Notification.objects.create(
                type_notif='Add_Comment',
                from_user=from_user,
                to_user=to_user,
                post=instance.post,
                comment_post=instance
            )

@receiver(post_save, sender=Relationship)
def post_save_add_notif_relations(sender, instance, created, **kwargs):
    from_user = instance.sender.user
    to_user = instance.receiver.user
    
    if instance.status == 'accepted':
        if Notification.objects.filter(type_notif='invitation_accepted', from_user=to_user, to_user=from_user).exists():
            notif = Notification.objects.get(type_notif='invitation_accepted', from_user=to_user, to_user=from_user)
            # notif.date_created = timezone.now(); 
            notif.seen = False; notif.bg_seen = False
            notif.save()
        else:
            Notification.objects.create(
                type_notif='invitation_accepted',
                from_user=to_user, 
                to_user=from_user
            )
        
    elif instance.status == 'send':
        if Notification.objects.filter(type_notif='invitation_send', from_user=from_user, to_user=to_user).exists():
            notif = Notification.objects.get(type_notif='invitation_send', from_user=from_user, to_user=to_user)
            # notif.date_created = timezone.now(); 
            notif.seen = False; notif.bg_seen = False
            notif.save()
        else:
            Notification.objects.create(
                type_notif='invitation_send',
                from_user=from_user,
                to_user=to_user
            )

@receiver(pre_delete, sender=Relationship)
def pre_delete_notif_relations(sender, instance, **kwargs):
    from_user = instance.sender.user
    to_user = instance.receiver.user
    
    if instance.status == 'accepted':
        if Notification.objects.filter(type_notif='invitation_accepted', from_user=to_user, to_user=from_user).exists():
            notif = Notification.objects.filter(type_notif='invitation_accepted', from_user=to_user, to_user=from_user)
            notif.delete()
        if Notification.objects.filter(type_notif='invitation_send', from_user=from_user, to_user=to_user).exists():
            notif = Notification.objects.filter(type_notif='invitation_send', from_user=from_user, to_user=to_user)
            notif.delete()
        
    elif instance.status == 'send':
        if Notification.objects.filter(type_notif='invitation_accepted', from_user=to_user, to_user=from_user).exists():
            notif = Notification.objects.filter(type_notif='invitation_accepted', from_user=to_user, to_user=from_user)
            notif.delete()
        if Notification.objects.filter(type_notif='invitation_send', from_user=from_user, to_user=to_user).exists():
            notif = Notification.objects.filter(type_notif='invitation_send', from_user=from_user, to_user=to_user)
            notif.delete()
