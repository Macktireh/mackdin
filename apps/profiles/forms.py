from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from apps.profiles.models import Profile

User = get_user_model()

class ProfileForm(forms.ModelForm):
    # img_profile = forms.ImageField(required=False, widget=forms.FileInput(
    #     attrs={'class':'form-control-profile'}))
    # img_bg = forms.ImageField(required=False, widget=forms.FileInput(
    #     attrs={'class':'form-control-profile'}))
    # img_profile_clear = forms.BooleanField(required=False, widget=forms.CheckboxInput(
    #     attrs={'class':'form-control-profile'}))
    class Meta:
        model = Profile
        exclude = ('user', 'number_views', 'gender', 'birth_date', 'friends',)
        widgets = {
            'pseudo': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'bio': forms.TextInput(attrs={'class': 'form-control-profile'}),
            # 'img_profile': forms.FileInput(attrs={'class': 'form-control-profile'}),
            # 'img_bg': forms.FileInput(attrs={'class': 'form-control-profile'}),
            'phone': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'adress': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'town': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'region': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'country': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'description': forms.Textarea(attrs={'cols':'80', 'rows':'8', 'class': 'form-control-profile'}),
            'link_linkedin': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'link_gitthub': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'link_twitter': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'link_mysite': forms.TextInput(attrs={'class': 'form-control-profile'}),
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control-profile'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control-profile'}),

        }
        