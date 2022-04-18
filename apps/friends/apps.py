from django.apps import AppConfig


class FriendsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.friends'
    
    def ready(self):
        import apps.friends.signals
