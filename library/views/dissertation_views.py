from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import DissertationModelForm
from library.models import Dissertation, Review
from library.views import FileUploadMixin
from users.mixins import StaffRequiredMixin


class DissertationListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Dissertation
    context_object_name = 'dissertations'
    ordering = ['-add_date']
    template_name = 'library/dissertation/dissertation_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Диссертации'}


class DissertationDetailView(LoginRequiredMixin, DetailView):
    model = Dissertation
    context_object_name = 'dissertation'
    slug_field = 'slug'
    template_name = 'library/dissertation/dissertation_detail.html'
    extra_context = {'title': 'Просмотр диссертации'}


class DissertationCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView, FileUploadMixin):
    model = Dissertation
    success_url = reverse_lazy('library:dissertation-list')
    template_name = 'library/dissertation/dissertation_create_form.html'
    form_class = DissertationModelForm
    extra_context = {'title': 'Добавить диссертацию'}
    file_field_name = 'reviews'

    def create_related_object(self, file):
        Review.objects.create(dissertation=self.object, file=file)


class DissertationUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView, FileUploadMixin):
    model = Dissertation
    form_class = DissertationModelForm
    success_url = reverse_lazy('library:dissertation-list')
    template_name = 'library/dissertation/dissertation_create_form.html'
    extra_context = {'title': 'Изменить диссертацию'}
    file_field_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['reviews'] = Review.objects.filter(dissertation=self.object).all()
        return context

    def create_related_object(self, file):
        Review.objects.create(dissertation=self.object, file=file)


class DissertationDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Dissertation
    context_object_name = 'dissertation'
    slug_field = 'slug'
    success_url = reverse_lazy('library:dissertation-list')
    extra_context = {'title': 'Удалить диссертацию'}
