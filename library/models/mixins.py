from django.db import models
from django.core.validators import RegexValidator
from .science_work import child_files_save_path


class GOVRegisterMixin(models.Model):
    doc_num = models.CharField('Номер свидетельства', null=False, db_index=True, max_length=64,
                               validators=[RegexValidator(
                                   regex=r"^\d+$",
                                   message="Номер должен содержать только цифры"
                               )])
    implementation_act = models.FileField('Файл акта реализации', upload_to=child_files_save_path,
                                          null=True, blank=True)

    class Meta:
        abstract = True


class UDCMixin(models.Model):
    udc = models.CharField('УДК', null=False, db_index=True, max_length=64)

    class Meta:
        abstract = True


class ISBNMixin(models.Model):
    isbn = models.CharField('Международный стандартный книжный номер (ISBN)',
                            null=True, blank=True, max_length=16, db_index=True,
                            validators=[RegexValidator(
                                regex=r"^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$",
                                message="Некорректный ISBN-номер"
                            )])

    class Meta:
        abstract = True


# class DOIMixin(models.Model):
#     doi = models.CharField('DOI', null=True, blank=True, db_index=True, max_length=128)
#
#     class Meta:
#         abstract = True






