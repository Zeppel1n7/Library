from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig


AuthConfig.verbose_name = "Групповая политика"


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    label = 'users'
    verbose_name = "Пользователи"
