from django.apps import AppConfig


class SespConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sesp'
    def ready(self):
        import sesp.signals
