from .science_work import ScienceWork
from .mixins import ISBNMixin, UDCMixin


class Monograph(ScienceWork, ISBNMixin, UDCMixin):

    def get_absolute_url(self):
        return f"/monograph/{self.slug}"

    def __str__(self):
        return f"Монография: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'монография'
        verbose_name_plural = 'монографии'
        db_table = 'monograph'
