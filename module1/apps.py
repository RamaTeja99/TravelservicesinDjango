from django.apps import AppConfig


class Module1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'module1'


class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'