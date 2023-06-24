from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q


class ProfileManager(models.Manager):
    def get_all_profiles_exclude_me(self, request, me):
        """
        me : utilisateur connecté

        Returns:
            cette méthode renvoie tous les profils à l'exception de l'utilisateur connecté
        """
        from apps.profiles.models import Profile

        profiles = (
            Profile.objects.select_related("user")
            .prefetch_related("sender")
            .filter(user__is_email_verified=True)
            .exclude(user=me)
        )
        # paginator = Paginator(_profiles, 10)
        # page_number = request.GET.get("page")
        # profiles = paginator.get_page(page_number)

        return profiles

    def get_all_profiles_to_invites(self, request, sender):
        """
        Args:
            sender : utilisateur qui envoie l'invitation

        Returns:
            cette méthode renvoie tous les profils qui ne sont pas liés à l'utilisateur connecté
        """
        from apps.friends.models import Relationship
        from apps.profiles.models import Profile

        profile = Profile.objects.get(user=sender)

        _profiles = (
            Profile.objects.select_related("user")
            .prefetch_related("sender")
            .filter(user__is_email_verified=True)
            .exclude(user=sender)
        )
        paginator = Paginator(_profiles, 30)
        page_ = request.GET.get("page")
        num_ = paginator.num_pages

        if page_ is None:
            page_ = 1
        if int(page_) > num_:
            raise ValueError("")

        profiles = paginator.get_page(page_)

        _qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))
        paginator = Paginator(_qs, 30)
        _page = request.GET.get("page")
        _num = paginator.num_pages

        if _page is None:
            _page = 1
        if num_ < _num:
            if int(_page) > _num:
                raise ValueError("")
        qs = paginator.get_page(_page)

        accepted = set([])
        for q in qs:
            if q.status == "accepted":
                accepted.add(q.receiver)
                accepted.add(q.sender)

        available = [_profile for _profile in profiles if _profile not in accepted]

        return available
