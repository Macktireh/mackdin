from threading import Thread
from typing import Any, Dict, List

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template, render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _


from apps.users.token import generate_token


def send_email_activation_account(user, request):
    current_site = get_current_site(request)
    email_subject_activate = f"Confirmer votre adresse email de votre compte Mackdin"
    email_body_activate = render_to_string(
        "users/actiavte.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user),
        },
    )
    email = EmailMessage(
        subject=email_subject_activate,
        body=email_body_activate,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.send()


def send_email_activation_account_success(user, request):
    current_site = get_current_site(request)
    email_subject_activate_success = (
        f"{current_site} - Votre compte a été créé et activé avec succès !"
    )
    email_body_activate_success = render_to_string(
        "users/actiavte_success.html",
        {
            "domain": current_site,
        },
    )
    email = EmailMessage(
        subject=email_subject_activate_success,
        body=email_body_activate_success,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.send()


def email_sender(user, request, subject, template):
    body = render_to_string(
        template,
        {
            "domain": get_current_site(request),
        },
    )
    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.send()


def sendAsyncEmail(eamil: EmailMessage) -> None:
    try:
        eamil.send()
    except ConnectionRefusedError:
        raise ValueError("Connection refused")
    except TemplateDoesNotExist:
        raise TemplateDoesNotExist("The template does not exist")


def send_email(
    subject: str,
    context: Dict[str, Any],
    to: List[str],
    template_name: str | None = None,
    _from: str = settings.EMAIL_HOST_USER,
) -> None:
    try:
        if template_name is None:
            raise TemplateDoesNotExist("The template does not exist")
        ext = template_name.split(".")[-1]
        htmlContent = get_template(template_name).render(context)
        email = EmailMessage(
            subject=subject,
            body=htmlContent,
            from_email=_from,
            to=to,
        )
        if ext == "html":
            email.content_subtype = "html"
        Thread(target=sendAsyncEmail, args=(email,)).start()
    except TemplateDoesNotExist:
        raise TemplateDoesNotExist("The template does not exist")
