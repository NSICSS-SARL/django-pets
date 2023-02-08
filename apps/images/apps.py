from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.images'

    def ready(self):
        # import signal handlers
        import apps.images.signals
