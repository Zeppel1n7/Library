from .science_work import ScienceWork
from .mixins import UDCMixin


class Dissertation(ScienceWork, UDCMixin):

    def get_absolute_url(self):
        return f"/dissertation/{self.slug}"

    def __str__(self):
        return f"Диссертация: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'диссертация'
        verbose_name_plural = 'диссертации'
        db_table = 'dissertation'
