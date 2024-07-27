import os
import uuid
from django.db import models
from library.utils import unique_slugify


def parent_save_path(instance, filename):
    return os.path.join(f"work_{instance.id}", filename)


def child_files_save_path(instance, filename):
    return os.path.join(f"work_{instance.sciencework_ptr.id}", filename)


class ScienceWork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Название', max_length=256, null=False, db_index=True)
    annotation = models.TextField('Аннотация (описание)', null=False)
    is_secret = models.BooleanField('Для служебного пользования', null=False)
    slug = models.SlugField('Слаг работы', max_length=128, unique=True, db_index=True, null=False)
    publication_date = models.DateField('Дата публикации работы', null=False)
    add_date = models.DateField('Дата добавления', auto_now_add=True)
    conclusion_file = models.FileField('Файл заключения', upload_to=parent_save_path, null=False)
    file = models.FileField('Файл работы', upload_to=parent_save_path, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name, max_length=128)
        super(ScienceWork, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/work/{self.slug}"

    def __str__(self):
        return f"{self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'научная работа'
        verbose_name_plural = 'научные работы'
        db_table = 'science_work'
        get_latest_by = 'add_date'
