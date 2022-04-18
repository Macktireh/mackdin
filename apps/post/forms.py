from django import forms
from django.forms import fields
from apps.post.models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    """Form definition for Post."""
    message = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows':'2', 'id':'textarea_id', 'placeholder':'Ajouter un post'}))
    img = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'id':'file', 'class':'form-input-file'}))
    class Meta:
        """Meta definition for Postform."""
        model = Post
        fields = ('message', 'img',)

    def clean(self, *args, **kwargs):
        msg = self.cleaned_data.get('message')
        img = self.cleaned_data.get('img')
        if (msg is None or msg == '') and (img is None):
            raise forms.ValidationError(_("Veuillez entrer un message ou charger une image"))