import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from cloudinary.models import CloudinaryField
from apps.utils.function import rename_post_img_video

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    uid = models.CharField(_("code post"), max_length=500, blank=True)
    message = models.TextField(_("message"), blank=True)
    
    # cloudinary will be used to upload images and videos eslse
    img = CloudinaryField(_("image"), blank=True, null=True)
    # img = models.ImageField(_("image"), upload_to=rename_post_img_video, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])], blank=True, null=True)
    video = models.FileField(_("video"), upload_to=rename_post_img_video, blank=True, null=True)
    date_created = models.DateTimeField(_("date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)
    liked = models.ManyToManyField(User, related_name='user_like', blank=True, default=None)

    def __str__(self):
        return f"Post-{self.id}-{self.author.first_name}"
    
    def save(self, *args, **kwargs):
        if self.uid == "":
            self.uid = str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(self.id)
        return super().save(*args, **kwargs)
    
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