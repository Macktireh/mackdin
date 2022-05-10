from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from apps.users.token import generate_token

def send_email_activation_account(user, request):
    current_site = get_current_site(request)
    email_subject_activate = f"Confirmer votre adresse email de votre compte Mackdin"
    email_body_activate = render_to_string('users/actiavte.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        }
    )
    email = EmailMessage(
        subject=email_subject_activate,
        body=email_body_activate,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    email.send()

def send_email_activation_account_success(user, request):
    current_site = get_current_site(request)
    email_subject_activate_success = f"{current_site} - Votre compte a été créé et activé avec succès !"
    email_body_activate_success = render_to_string('users/actiavte_success.html', {'domain': current_site,})
    email = EmailMessage(
        subject=email_subject_activate_success,
        body=email_body_activate_success,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    email.send()