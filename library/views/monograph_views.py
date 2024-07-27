from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import MonographModelForm
from library.models import Monograph, Review
from library.views import FileUploadMixin
from users.mixins import StaffRequiredMixin


class MonographListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Monograph
    context_object_name = 'monographs'
    ordering = ['-add_date']
    template_name = 'library/monograph/monograph_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Монографии'}


class MonographDetailView(LoginRequiredMixin, DetailView):
    model = Monograph
    context_object_name = 'monograph'
    slug_field = 'slug'
    template_name = 'library/monograph/monograph_detail.html'
    extra_context = {'title': 'Просмотр монографии'}


class MonographCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView, FileUploadMixin):
    model = Monograph
    success_url = reverse_lazy('library:monograph-list')
    template_name = 'library/monograph/monograph_create_form.html'
    form_class = MonographModelForm
    extra_context = {'title': 'Добавить монографию'}
    file_field_name = 'reviews'

    def create_related_object(self, file):
        Review.objects.create(monograph=self.object, file=file)


class MonographUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView, FileUploadMixin):
    model = Monograph
    form_class = MonographModelForm
    success_url = reverse_lazy('library:monograph-list')
    template_name = 'library/monograph/monograph_create_form.html'
    extra_context = {'title': 'Изменить монографию'}
    file_field_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['reviews'] = Review.objects.filter(monograph=self.object).all()
        return context

    def create_related_object(self, file):
        Review.objects.create(monograph=self.object, file=file)


class MonographDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Monograph
    context_object_name = 'monograph'
    slug_field = 'slug'
    success_url = reverse_lazy('library:monograph-list')
    extra_context = {'title': 'Удалить монографию'}
