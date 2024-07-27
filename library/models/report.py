# from .science_work import ScienceWork
# from .mixins import UDCMixin
#
#
# class Report(ScienceWork, UDCMixin):
#
#     def get_absolute_url(self):
#         return f"/report/{self.slug}"
#
#     def __str__(self):
#         return f"Отчет: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"
#
#     class Meta:
#         verbose_name = 'отчет'
#         verbose_name_plural = 'отчеты'
#         db_table = 'report'
