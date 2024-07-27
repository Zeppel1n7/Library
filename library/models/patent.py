from django.db import models
from .science_work import ScienceWork
from .mixins import GOVRegisterMixin


class Patent(ScienceWork, GOVRegisterMixin):
    class PatentTypes(models.TextChoices):
        UTILITY_MODEL = "UM", "Полезная модель"
        INVENTION = "INV", "Изобретение"
        INDUSTRIAL_MODEL = 'IM', 'Промышленный образец'

    patent_type = models.CharField('Тип патента', max_length=8, null=False,
                                   choices=PatentTypes, default=PatentTypes.UTILITY_MODEL)

    patent_owner = models.CharField('Патентообладатель', max_length=256, null=False)

    def get_absolute_url(self):
        return f"/patent/{self.slug}"

    def __str__(self):
        return f"Патент: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'патент'
        verbose_name_plural = 'патенты'
        db_table = 'patent'
