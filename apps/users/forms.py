import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm

from apps.users.models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        

class Sign_UpForm(forms.ModelForm):
    first_name = forms.CharField(label='Prénom', min_length=2, required=True, widget=forms.TextInput(
        attrs={'id': 'firstname', 'class': 'form-control', 'autocomplete': 'off'}))
    
    last_name = forms.CharField(label='Nom', min_length=2, required=True, widget=forms.TextInput(
        attrs={'id': 'lastname', 'class': 'form-control', 'autocomplete': 'off'}))
    
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'id': 'email', 'class': 'form-control', 'autocomplete': 'off'}))
    
    password = forms.CharField(label='Mot de pass', required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'class': 'form-control', 'autocomplete': 'off'}))
    
    confirm_password = forms.CharField(label='Confimer le mot de pass', required=True, widget=forms.PasswordInput(
        attrs={'id': 'confirm', 'class': 'form-control', 'autocomplete': 'off'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        
    def signup_email_validation(self, email):
        return True if re.match(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        , email) else False

    def signup_password_validation(self, password):
        return True if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password) else False

    def signup_password_validation_confirm(self, password, confirme_password):
        return password == confirme_password   

    def clean_first_name(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        # print('first_name :', first_name)
        if first_name is None:
            raise forms.ValidationError(_("Le champ prénom ne doit pas être vide !"))
        elif len(first_name) < 2:
            raise forms.ValidationError(_("Le champ prénom n'est pas valide !"))
        return first_name

    def clean_last_name(self, *args, **kwargs):
        last_name = self.cleaned_data.get('last_name')
        # print('last_name :', last_name)
        if last_name is None:
            raise forms.ValidationError(_("Le champ nom ne doit pas être vide !"))
        elif len(last_name) < 2:
            raise forms.ValidationError(_("Le champ nom n'est pas valide !"))
        return last_name

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        # print('email :', email)
        if not self.signup_email_validation(email):
            raise forms.ValidationError(_("Le champ email n'est pas valide!"))
        return email

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        # print('password :', password)
        if not self.signup_password_validation(password):
            raise forms.ValidationError(_("Le champ mot de passe doit contenir: minimum de 8 caractères, au moins majuscule et minuscule, au moins chiffre et un caractère spécial."))
        return password

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        # print('password :', password)
        # print('confirm_password :', confirm_password)
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(_("Les mots de passe ne correspondent pas"))

