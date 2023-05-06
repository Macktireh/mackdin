import os
import uuid
import cloudinary
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from config.settings import ENV

User = get_user_model()
from apps.profiles.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        if instance.first_name is not None or instance.first_name != '':
            instance.profile.pseudo = f'{instance.first_name}{instance.pk}'
        if instance.profile.uid == "":
            instance.profile.uid = str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(instance.id)
        instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.profile.pseudo == '':
        if instance.first_name is not None or instance.first_name != '':
            instance.profile.pseudo = f'{instance.first_name}{instance.pk}'.lower()
        instance.profile.save()
    if instance.profile.uid == "":
        instance.profile.uid = str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(instance.id)
        instance.profile.save()

@receiver(pre_delete, sender=Profile)
def image_delete(sender, instance, **kwargs):
    if ENV == 'production':
        if instance.img_profile:
            if instance.is_updating_img_profile:
                cloudinary.uploader.destroy(str(instance.img_profile))
        if instance.img_bg:
            if instance.is_updating_img_bg:
                cloudinary.uploader.destroy(str(instance.img_bg))
    else:
        if instance.img_profile:
            if instance.is_updating_img_profile:
                try:
                    os.remove(instance.img_profile.path)
                except:
                    cloudinary.uploader.destroy(str(instance.img_profile))
        if instance.img_bg:
            if instance.is_updating_img_bg:
                try:
                    os.remove(instance.img_bg.path)
                except:
                    cloudinary.uploader.destroy(str(instance.img_bg))