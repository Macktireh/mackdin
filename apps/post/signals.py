import cloudinary
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from apps.post.models import Post

@receiver(pre_delete, sender=Post)
def image_delete(sender, instance, **kwargs):
    if instance.img:
        cloudinary.uploader.destroy(instance.img.public_id)
