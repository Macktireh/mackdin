from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.utils.translation import gettext as _

from apps.friends.models import Relationship
from apps.profiles.models import Profile


User = get_user_model()


def num_friends(request):
    qs = Profile.objects.get_all_profiles_exclude_me(request, request.user)
    num_friends = 0
    for friend in qs:
        num_friends += request.user in friend.friends.all()
    return num_friends


def is_ajax(request: HttpRequest):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def list_relation_receiver_and_sender(request):
    qs = Profile.objects.get_all_profiles_to_invites(request, request.user)
    profile = Profile.objects.get(user=request.user)

    list_relation_receiver = [
        item.receiver.user
        for item in Relationship.objects.select_related("receiver").filter(
            sender=profile
        )
    ]
    list_relation_sender = [
        item.sender.user
        for item in Relationship.objects.select_related("sender").filter(
            receiver=profile
        )
    ]

    # paginator = Paginator(qs, 24)
    # page = request.GET.get("page")
    # num = paginator.num_pages

    # if page is None:
    #     page = 1
    # if int(page) > num:
    #     raise ValueError("")

    # qs = paginator.get_page(page)

    num = 0
    for obj in qs:
        num += (
            obj.user not in list_relation_receiver
            and obj.user not in list_relation_sender
        )
    is_empty = num == 0

    template = "friends/mynetwork.html"
    context = {
        "qs": qs,
        "list_receiver": list_relation_receiver,
        "list_sender": list_relation_sender,
        "is_empty": is_empty,
    }

    return template, context


def statistic_relationship_receiver(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    num_invitation_received = Relationship.objects.invatation_received(profile).count()
    num_invitation_send = Relationship.objects.invatation_sended(profile).count()

    dict_stat_context = {
        "num_friends": num_friends(request),
        "num_invitation_received": num_invitation_received,
        "num_invitation_send": num_invitation_send,
    }

    return dict_stat_context


# Vue de tous utiliateurs qui ne sont pas ami (avec moi => utilisateur connecté) et il y'a aucune invitation et reception
@login_required(login_url="sign_in")
def invites_list_profiles_view(request: HttpRequest) -> HttpResponse:
    try:
        template, context = list_relation_receiver_and_sender(request)
    except ValueError:
        return HttpResponseNotFound("<h1>Page not found 404</h1>")
    context.update(
        {
            "page": "list_not_friends",
            "start_animation": "my_network",
            "h3": _("Personnes à qui vous pourriez envoyer une invitation"),
            "h3_empty": _("Pas de profils avec lesquels interagir"),
        }
    )
    context.update(statistic_relationship_receiver(request))

    if request.is_ajax():
        return render(request, "friends/components/invites_list_profiles.html", context)

    return render(request, template, context)


# fonction pour envoyer une invitation aux utilisateurs
def send_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_id")
        red_to = request.POST.get("redirect")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        relation = Relationship.objects.create(
            sender=sender,
            receiver=receiver,
            status="send",
            date_sender=timezone.now(),
            date_receiver=timezone.now(),
        )
    if red_to == "profile":
        return redirect("profiles:profile", pseudo=receiver.pseudo)
    else:
        return redirect("friends:my_network")


# Vue des profiles amis
@login_required(login_url="sign_in")
def my_friends_invites_profiles_view(request):
    # qs = Profile.objects.get_all_profiles_exclude_me(request, request.user)

    profile = Profile.objects.get(user=request.user)
    paginator = Paginator(profile.friends.all(), 8)
    page = request.GET.get("page")
    num = paginator.num_pages

    if page is None:
        page = 1
    if int(page) > num:
        return HttpResponseNotFound("<h1>Page not found 404</h1>")

    _profile = paginator.get_page(page)

    qs = []
    for friend in _profile:
        qs.append(friend.profile)

    is_empty = num_friends(request) == 0

    template = "friends/mynetwork.html"
    context = {
        "qs": qs,
        "page": "my_friends",
        "start_animation": "my_network",
        "is_empty": is_empty,
        "h3": _("Vos relations"),
        "h3_empty": _("Pas de profils avec lesquels interagir"),
    }

    context.update(statistic_relationship_receiver(request))

    if request.is_ajax():
        return render(request, "friends/components/list_myfriends.html", context)

    return render(request, template, context)


# Vue pour surpprimer les profiles amis
def remove_from_friends(request):
    if request.method == "POST":
        pk = request.POST.get("profile_id")
        red_to = request.POST.get("redirect")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        relation = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver))
            | (Q(sender=receiver) & Q(receiver=sender))
        )
        relation.delete()
    if red_to == "profile":
        return redirect("profiles:profile", pseudo=receiver.pseudo)
    else:
        return redirect("friends:my_friends")


# Vue des invitation reçu
@login_required(login_url="sign_in")
def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invatation_received(profile)
    is_empty = len(qs) == 0

    template = "friends/mynetwork.html"
    context = {
        "qs": qs,
        "page": "invitation_received",
        "start_animation": "my_network",
        "is_empty": is_empty,
        "h3": _("Invitations en attente que vous acceptez"),
        "h3_empty": _("Aucune invitation reçue en attente"),
    }

    context.update(statistic_relationship_receiver(request))

    return render(request, template, context)


# Vue pour accepter les invitation reçu
def accept_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_id")
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        relation = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if relation.status == "send":
            relation.status = "accepted"
            relation.save()
            return redirect("friends:invitation_received")
    return redirect("friends:invitation_received")


# Vue pour refuser les invitation reçu
def reject_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_id")
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        relation = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        relation.delete()
    return redirect("friends:invitation_received")


# Vue pour les invitation envoyer
@login_required(login_url="sign_in")
def invites_sended_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invatation_sended(profile)
    is_empty = len(qs) == 0

    template = "friends/mynetwork.html"
    context = {
        "qs": qs,
        "page": "invitation_send",
        "start_animation": "my_network",
        "is_empty": is_empty,
        "h3": "Les invitations envoyer qui sont en cours d'acceptation",
        "h3_empty": _("Pas d'invitations envoyées qui sont en cours d'acceptation"),
    }

    context.update(statistic_relationship_receiver(request))

    return render(request, template, context)


# Vue pour annuler les invitation envoyer
def cancel_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_id")
        sender = Profile.objects.get(user=request.user)
        receiver = Profile.objects.get(pk=pk)
        relation = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        relation.delete()
    return redirect("friends:invitation_send")
