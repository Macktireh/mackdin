import os
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField

User = get_user_model()
from apps.profiles.managers import ProfileManager


def rename_img(instance, filename):
    upload_to = 'image_profile'
    ext = filename.split('.')[-1]
    filename = f"{instance.user.first_name}_{instance.user.pk}_{instance.date_updated.strftime('%d-%m-%Y %H%M%S')}.{ext}"
    folder = f"{instance.user.first_name}_{instance.user.pk}"
    return os.path.join('media', folder, upload_to, filename)

def pseudo_rename(instance, filename):
    upload_to = 'image_profile'
    ext = filename.split('.')[-1]
    filename = f"{instance.user.first_name}_{instance.user.pk}_{instance.date_updated}.{ext}"
    return os.path.join(upload_to, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    pseudo = models.CharField(_("non d'utilisateur"), max_length=48, blank=True, unique=True)
    bio = models.CharField(_("titre du profil"), max_length=250, blank=True)
    # img_profile = models.ImageField(_("photo de profile"), upload_to=rename_img, default='default/default-img-profile.jpg', blank=True, null=True)
    # img_bg = models.ImageField(_("photo de couverture"), upload_to=rename_img, default='default/default-img-bg.jpg', blank=True, null=True)
    img_profile = CloudinaryField('photo de profile', blank=True, null=True, default="https://res.cloudinary.com/dm68aag3e/image/upload/v1649743168/default-img-profile_hrhx6z.jpg")
    img_bg = CloudinaryField('photo de couverture', blank=True, null=True, default="https://res.cloudinary.com/dm68aag3e/image/upload/v1649743327/default-img-bg_zbeoo4.jpg")
    birth_date = models.DateField(_("date de naissence"), null=True, blank=True)
    
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
    link_linkedin = models.URLField(_("lien de votre profile linkedin"), blank=True)
    link_gitthub = models.URLField(_("lien de votre profile gitthub"), blank=True)
    link_twitter = models.URLField(_("lien de votre twitter"), blank=True)
    link_mysite = models.URLField(_("lien de votre de site web"), blank=True)
    number_views = models.IntegerField(_('Nombre de vue profil'), default=0, blank=True, null=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')    
    date_updated = models.DateTimeField(_("date de modification"), auto_now=True)
    
    objects = ProfileManager()
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def get_friends(self):
        return self.friends.all()
    
    def get_number_friends(self):
        return self.friends.all().count()
    
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
    
