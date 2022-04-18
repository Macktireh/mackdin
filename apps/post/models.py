import os
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from datetime import datetime
from cloudinary.models import CloudinaryField

User = get_user_model()

def rename_img_video(instance, filename):
    ext = filename.split('.')[-1]
    name = ''
    for i in range((len(filename.split('.'))-1)):
        name += filename.split('.')[i]
    filename = f"{name}_{datetime.now().strftime('%d-%m-%Y %H%M%S')}.{ext}"
    folder = f"{instance.author.first_name}_{instance.author.pk}"
    if ext.lower() in ['png', 'jpg', 'jpeg', 'gif']:
        return os.path.join('media', folder, 'image_post', filename)
    return os.path.join('media', folder, 'video_post', filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    message = models.TextField(_("message"), blank=True)
    # img = models.ImageField(_("image"), upload_to=rename_img_video, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])], blank=True, null=True)
    img = CloudinaryField(_("image"), blank=True, null=True)
    video = models.FileField(_("video"), upload_to=rename_img_video, blank=True, null=True)
    date_created = models.DateTimeField(_("date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)
    liked = models.ManyToManyField(User, related_name='user_like', blank=True, default=None)

    def __str__(self):
        return f"Post-{self.id}-{self.author.first_name}"
    
    @property
    def number_of_like(self):
        return self.liked.all().count()
    
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date_created',)

class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    )
    value = models.CharField(choices=LIKE_CHOICES, max_length=10)
    
    def __str__(self):
        return f"Auteur: {self.user.first_name} {self.user.last_name}   -   PostId: {self.post.id}"