from django.apps import AppConfig
from django_cleanup.signals import cleanup_post_delete
from library.handlers import clear_empty_dirs


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
    label = 'library'
    verbose_name = "Библиотека"

    def ready(self):
        cleanup_post_delete.connect(clear_empty_dirs)
