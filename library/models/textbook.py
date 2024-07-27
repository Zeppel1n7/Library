import os
from django.db import models
from .science_work import ScienceWork
from .mixins import ISBNMixin, UDCMixin


def stc_certificate_file_path(instance, filename):
    return os.path.join(f"work_{instance.sciencework_ptr_id}", filename)


class Textbook(ScienceWork, ISBNMixin, UDCMixin):
    STC_certificate = models.FileField('файл выписки из НТС',
                                       upload_to=stc_certificate_file_path, null=True, blank=True)

    def get_absolute_url(self):
        return f"/textbook/{self.slug}"

    def __str__(self):
        return f"Учебное пособие: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'учебное пособие'
        verbose_name_plural = 'учебные пособия'
        db_table = 'textbook'
