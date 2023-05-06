import os
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from cloudinary.models import CloudinaryField
from apps.profiles.managers import ProfileManager
from apps.utils.function import rename_profile_img
from config.settings import ENV

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.CharField(_("code identifiant"), max_length=500, blank=True)
    pseudo = models.CharField(_("non d'utilisateur"), max_length=48, blank=True, unique=True)
    bio = models.CharField(_("titre du profil"), max_length=250, blank=True)
    birth_date = models.DateField(_("date de naissence"), null=True, blank=True)
    
    # img_profile = CloudinaryField('photo de profile', blank=True, null=True, default="https://res.cloudinary.com/dm68aag3e/image/upload/v1649743168/default-img-profile_hrhx6z.jpg")
    # img_bg = CloudinaryField('photo de couverture', blank=True, null=True, default="https://res.cloudinary.com/dm68aag3e/image/upload/v1649743327/default-img-bg_zbeoo4.jpg")
    img_profile = models.ImageField(_("photo de profile"), upload_to=rename_profile_img, default="mediafiles/default/profile_jyytyz.jpg", blank=True, null=True)
    img_bg = models.ImageField(_("photo de couverture"), upload_to=rename_profile_img, default="mediafiles/default/bg_r0siq1.jpg", blank=True, null=True)
    img_profile_str = models.CharField(max_length=500, default="https://res.cloudinary.com/dm68aag3e/image/upload/v1649743168/default-img-profile_hrhx6z.jpg", blank=True, null=True)
    img_bg_str = models.CharField(max_length=500, default="https://res.cloudinary.com/dm68aag3e/image/upload/v1649743327/default-img-bg_zbeoo4.jpg", blank=True, null=True)
    is_fixture = models.BooleanField(default=False)
    is_updating_img_profile = models.BooleanField(_("is updating img profile"), default=False)
    is_updating_img_bg = models.BooleanField(_("is updating img bg"), default=False)
    class GenderChoices(models.TextChoices):
        male = 'M', _('Masculin')
        female = 'F', _('Féminin')
    
    gender = models.CharField(_("sexe"), max_length=1, blank=True, choices=GenderChoices.choices)
    phone = models.CharField(_("téléphone"), max_length=20, blank=True)
    adress = models.CharField(_("adresse"), max_length=128, blank=True)
    town = models.CharField(_("ville"), max_length=68, blank=True)
    region = models.CharField(_("région"), max_length=68, blank=True)
    zipcode = models.CharField(_("code postal"), max_length=22, blank=True)
    country = models.CharField(_("pays"), max_length=45, blank=True)
    description = models.TextField(_("description"), blank=True)
    link_linkedin = models.URLField(_("lien de votre profil linkedin"), blank=True)
    link_gitthub = models.URLField(_("lien de votre gitthub"), blank=True)
    link_twitter = models.URLField(_("lien de votre twitter"), blank=True)
    link_mysite = models.URLField(_("lien de votre site web"), blank=True)
    number_views = models.IntegerField(_('Nombre de vue profil'), default=0, blank=True, null=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')    
    date_updated = models.DateTimeField(_("date de modification"), auto_now=True)
    
    objects = ProfileManager()
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def save(self, *args, **kwargs):
        if self.uid == "":
            self.uid = str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(self.user.id)
        return super().save(*args, **kwargs)
    
    def get_friends(self):
        return self.friends.all()
    
    def get_number_friends(self):
        return self.friends.all().count()
    
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ['-date_updated']
        
    
