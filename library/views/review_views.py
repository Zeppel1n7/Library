from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from library.models import Review
from users.mixins import StaffRequiredMixin


class ReviewDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        article_id = self.object.article.id
        return reverse_lazy('article-update', kwargs={'pk': article_id})
