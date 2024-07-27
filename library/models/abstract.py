from .science_work import ScienceWork
from .mixins import UDCMixin


class Abstract(ScienceWork, UDCMixin):

    def get_absolute_url(self):
        return f"/abstract/{self.slug}"

    def __str__(self):
        return f"Автореферат: {self.name} | {list(map(lambda x: str(x), self.authors.all()))}"

    class Meta:
        verbose_name = 'автореферат'
        verbose_name_plural = 'авторефераты'
        db_table = 'abstract'
