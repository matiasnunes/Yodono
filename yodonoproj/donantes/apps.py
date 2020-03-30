from django.apps import AppConfig

class DonantesConfig(AppConfig):
    name = 'donantes'

    def ready(self):
        import donantes.signals
