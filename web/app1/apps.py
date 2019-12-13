from django.apps import AppConfig

from .tasks import add

class App1Config(AppConfig):
    name = 'app1'
