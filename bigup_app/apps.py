from django.apps import AppConfig


class BigupAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bigup_app'

    def ready(self):
        import bigup_app.signals
