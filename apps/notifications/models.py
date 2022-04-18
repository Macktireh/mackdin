from datetime import datetime
from re import T
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
from apps.post.models import LikePost, Post
from apps.comments.models import Comment
from apps.friends.models import Relationship


class Notification(models.Model):
    class Meta:
        ordering = ['-date_created']
        
    class TypeNotifChoices(models.TextChoices):
        like = 'Like_Post', _('Like Post')
        post = 'Add_Post', _('Add Post')
        comment = 'Add_Comment', _('Add Comment')
        invitation_accepted = 'invitation_accepted', _('invitation accepted')
        invitation_send = 'invitation_send', _('invitation send')
        
    type_notif = models.CharField(_('type_notif'), max_length=30, choices=TypeNotifChoices.choices)
    from_user = models.ForeignKey(User, related_name='notif_from', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='notif_to', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='notif_post', on_delete=models.CASCADE, blank=True, null=True)
    like_post = models.ForeignKey(LikePost, related_name='notif_like_post', on_delete=models.CASCADE, blank=True, null=True)
    comment_post = models.ForeignKey(Comment, related_name='notif_comment_post', on_delete=models.CASCADE, blank=True, null=True)
    # relationship = models.ForeignKey(Relationship, related_name='notif_relationship', on_delete=models.CASCADE, blank=True, null=True)
    seen = models.BooleanField(default=False)
    bg_seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)