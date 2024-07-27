import os
from django.core.exceptions import ValidationError
from django.db import models
from .article import Article
from .textbook import Textbook
from .monograph import Monograph
from .dissertation import Dissertation


def review_save_path(instance, filename):
    work = instance.get_linked_work()
    return os.path.join(f"work_{work.sciencework_ptr.id}", filename)


class Review(models.Model):
    file = models.FileField('Файл рецензии', upload_to=review_save_path, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Статья', null=True, blank=True)
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE, related_name='reviews',
                                 verbose_name='Учебное пособие', null=True, blank=True)
    dissertation = models.ForeignKey(Dissertation, on_delete=models.CASCADE, related_name='reviews',
                                     verbose_name='Диссертация', null=True, blank=True)
    monograph = models.ForeignKey(Monograph, on_delete=models.CASCADE, related_name='reviews',
                                  verbose_name='Монография', null=True, blank=True)

    def get_list_works(self):
        return [self.article, self.textbook, self.dissertation, self.monograph]

    def get_linked_work(self):
        works = self.get_list_works()
        work = [w for w in works if w is not None]
        return work[0] if work else None

    def __str__(self):
        work = self.get_linked_work()
        return f'Рецензия: {self.file.name} на {work.name}'

    def clean(self):
        works = self.get_list_works()
        work_count = sum(map(bool, works))
        if not work_count:
            raise ValidationError("Не выбрана научная работа")
        elif work_count > 1:
            raise ValidationError('Выбрано больше одной научной работы')

    class Meta:
        verbose_name = 'файл рецензии'
        verbose_name_plural = 'файлы рецензий'
        db_table = 'review_file'
