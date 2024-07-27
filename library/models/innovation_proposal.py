from django.db import models
from .science_work import ScienceWork, child_files_save_path
from .mixins import GOVRegisterMixin


class InnovationProposal(ScienceWork, GOVRegisterMixin):
    certificate = models.FileField('Удостоверение на рацпредложение', null=False, upload_to=child_files_save_path)

    def get_absolute_url(self):
        return f"/proposal/{self.slug}"

    def __str__(self):
        return f"Рацпредложение: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'рацпредложение'
        verbose_name_plural = 'рацпредложения'
        db_table = 'innovation_proposal'
