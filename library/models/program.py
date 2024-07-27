from .science_work import ScienceWork
from .mixins import GOVRegisterMixin


class Program(ScienceWork, GOVRegisterMixin):

    def get_absolute_url(self):
        return f"/program/{self.slug}"

    def __str__(self):
        return f"ПЭВМ: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'программа для ЭВМ'
        verbose_name_plural = 'программы для ЭВМ'
        db_table = 'program'
