import os
from EraLibrary import settings


def clear_empty_dirs(**kwargs):
    print('START DELETING')
    for path, dirs, files in os.walk(settings.MEDIA_ROOT, topdown=False):
        if path == settings.MEDIA_ROOT:
            break
        try:
            os.rmdir(path)
        except OSError as ex:
            pass
