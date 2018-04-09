from django.apps import AppConfig


class CryptocoinsConfig(AppConfig):
    name = 'cryptocoins'

    def ready(self):
        from . import signals
