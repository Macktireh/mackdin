from django.contrib.sites.shortcuts import get_current_site
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from allauth.account.signals import user_signed_up

from apps.users.email import send_email


@receiver(
    user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up"
)
def user_signed_up_(request, user, **kwargs):
    user.is_email_verified = True
    user.save()
    send_email(
        subject=_("Bienvenue sur Mackdin !"),
        context={"user": user, "domain": get_current_site(request)},
        to=[user.email],
        template_name="users/email-welcome.html",
    )
