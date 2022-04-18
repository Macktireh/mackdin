from django import forms
from django.forms import fields
from django.utils.translation import gettext_lazy as _

from apps.comments.models import Comment, ReponseComment


class CommentForm(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'id':'input_message_comment_id', 'autocomplete': 'off', 'placeholder':'Ajouter un commentaire...'}))
    class Meta:
        model = Comment
        fields = ('message',)
    

class ReponseCommentForm(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'id':'input_message_reponse_comment_id', 'autocomplete': 'off', 'placeholder':'Ajouter une réponse...'}))
    class Meta:
        model = ReponseComment
        fields = ('message',)