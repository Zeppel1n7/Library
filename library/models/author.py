import uuid
from django.db import models
from EraLibrary import settings
from .science_work import ScienceWork


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Пользователь',
                                related_name='author', null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField('Имя', max_length=64, null=False)
    last_name = models.CharField('Фамилия', max_length=64, null=False)
    patronymic = models.CharField('Отчество', max_length=64, blank=True, null=True)
    division = models.CharField('Подразделение', max_length=64, null=False)
    rank = models.CharField('Звание', max_length=64, null=False)

    science_works = models.ManyToManyField(ScienceWork, verbose_name='Научные работы',
                                           db_table='authors_works', blank=True,
                                           related_name='authors')

    class Meta:
        verbose_name = 'автора'
        verbose_name_plural = 'авторы'
        db_table = 'author'

    def get_short_name(self):
        return f'{self.last_name} {self.first_name[0].upper()}. {self.patronymic[0].upper()}.'

    def get_absolute_url(self):
        return f"/author/{self.id}/"

    def __str__(self):
        return f"{self.rank}: {self.get_short_name()}"
