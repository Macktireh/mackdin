import uuid
import cloudinary
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
from apps.profiles.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        if instance.first_name is not None or instance.first_name != '':
            instance.profile.pseudo = f'{instance.first_name}{instance.pk}'
        if instance.profile.uid == '':
            instance.profile.uid = str(uuid.uuid4()).replace('-', '')[:64] + str(instance.id)
        instance.profile.save()
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.profile.pseudo == '':
        if instance.first_name is not None or instance.first_name != '':
            instance.profile.pseudo = f'{instance.first_name}{instance.pk}'.lower()
    if instance.profile.uid == '':
        instance.profile.uid = str(uuid.uuid4()).replace('-', '')[:64] + str(instance.id)
    instance.profile.save()
    
    
    
@receiver(pre_delete, sender=Profile)
def image_delete(sender, instance, **kwargs):
    if instance.img_profile:
        cloudinary.uploader.destroy(instance.img_profile.public_id)
    if instance.img_bg:
        cloudinary.uploader.destroy(instance.img_bg.public_id)