import os
import uuid
import cloudinary
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from apps.post.models import Post
from config.settings import ENV


@receiver(post_save, sender=Post)
def save_uid_post(sender, instance, **kwargs):
    if instance.uid == "":
        instance.uid = str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(instance.id)
        instance.save()

@receiver(pre_delete, sender=Post)
def image_delete(sender, instance, **kwargs):
    if ENV == 'production':
        if instance.img:
            cloudinary.uploader.destroy(instance.img.public_id)
    else:
        if instance.img:
            os.remove(instance.img.path)
