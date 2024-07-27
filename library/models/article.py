from django.db import models
from django.core.validators import RegexValidator
from .science_work import ScienceWork
from .mixins import UDCMixin


class ScienceBase(models.Model):
    name = models.CharField('Научная база', max_length=128,
                            help_text='Научная база работы (ВАК, РИНЦ и т.д.)',
                            null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'научная база'
        verbose_name_plural = 'базы научных статей'
        db_table = 'science_base'


class Article(ScienceWork, UDCMixin):
    keywords = models.CharField('Ключевые слова', max_length=256, blank=True, null=True, db_index=True,
                                validators=[RegexValidator(
                                    regex=r"^\b(?:\s*[\wА-Яа-я\s]+\s*,?\s*)+\b$",
                                    message="Ключевые слова разделяются запятой",
                                )])
    science_base = models.ForeignKey(ScienceBase, on_delete=models.RESTRICT,
                                     related_name='science_base', verbose_name='Научная база работы')
    journal = models.CharField('Название сборника', max_length=256, null=False)

    def get_absolute_url(self):
        return f"/article/{self.slug}"

    def __str__(self):
        return f"Статья ({self.science_base}) {self.name}| {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'научная статья'
        verbose_name_plural = 'научные статьи'
        db_table = 'article'
