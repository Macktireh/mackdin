from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from apps.users.forms import Sign_UpForm
from apps.users.token import generate_token
from config.settings import EMAIL_HOST_USER

User = get_user_model()

def send_action_email(user, request):
    current_site = get_current_site(request)
    email_subject_activate = f"Confirmer votre adresse mail de votre compte sur {current_site}"
    email_body_activate = render_to_string('users/actiavte.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        }
    )
    email = EmailMessage(subject=email_subject_activate, body=email_body_activate, from_email=EMAIL_HOST_USER, to=[user.email])
    email.send()

def sign_up(request):
    if request.method == 'POST':
        user_form = Sign_UpForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, "Votre compte à été bien creér avec succès. Vous recevez un email pour confirmer votre adresse email.")
            current_site = get_current_site(request)
            
            # mail de bienvenue
            subject_welcome = f"Bienvenue {user.first_name} sur notre site"
            message_welcome = f"Bonjour {user.first_name} et Bienvenue sur notre site.\nNous très content de t'avoir parmis nous.\nMerci\nL'équipe {current_site}"
            from_email_welcome = EMAIL_HOST_USER
            to_email_welcome = [user.email]
            send_mail(subject_welcome, message_welcome, from_email_welcome, to_email_welcome, fail_silently=False)
            
            # mail d'activation du compte
            send_action_email(user, request)
            return redirect('sign_in')
        else:
            messages.error(request, "Merci de bien remplir les informations correctement.")
    else:
        user_form = Sign_UpForm()
    template = 'users/sign_up.html'
    context = {
        'user_form': user_form,
    }
    return render(request, template, context=context)
    

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if not user.is_email_verified:
                messages.warning(request, "Merci de confirmer d'abord votre adresse email.")
                return redirect('sign_in')
            else:
                login(request, user)
                return redirect('post:post_list')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "ERREUR : Votre mot de passe est incorrect.")
        else:
            messages.error(request, "ERREUR : Il semble que vous n'avez pas compte avec cette adresse email")
    template = 'users/sign_in.html'
    return render(request, template)


def user_logout(request):
    user = request.user
    user.last_logout = timezone.now()
    user.save()
    logout(request)
    return redirect('home:home')


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.success(request, "Votre email est vérifié avec succès. Vous pouvez vous connecter.")
        return redirect(reverse('sign_in'))
    template = 'users/activate_failed.html'
    context = {'user': user}
    return render(request, template, context=context)