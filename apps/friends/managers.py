from django.db import models


class RelationshipManager(models.Manager):
    def import_model(self):
        from apps.friends.models import Relationship

        return Relationship

    def invatation_received(self, receiver):
        """
        Args:
            receiver : invitation reçu
        Returns:
            cette méthode renvoie tous les profils
            pour lesquels vous avez reçu une invitation
        """
        qs = (
            self.import_model()
            .objects.select_related("receiver")
            .filter(receiver=receiver, status="send")
        )
        return qs

    def invatation_sended(self, sender):
        """
        Args:
            receiver : invitation reçu
        Returns:
            cette méthode renvoie tous les profils
            auxquels vous avez envoyé une invitation
        """

        qs = (
            self.import_model()
            .objects.select_related("sender")
            .filter(sender=sender, status="send")
        )
        return qs
