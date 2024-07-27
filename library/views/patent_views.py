from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import PatentModelForm
from library.models import Patent
from users.mixins import StaffRequiredMixin


class PatentListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Patent
    context_object_name = 'patents'
    ordering = ['-add_date']
    template_name = 'library/patent/patent_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Патенты'}


class PatentDetailView(LoginRequiredMixin, DetailView):
    model = Patent
    context_object_name = 'patent'
    slug_field = 'slug'
    template_name = 'library/patent/patent_detail.html'
    extra_context = {'title': 'Просмотр патента'}


class PatentCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Patent
    success_url = reverse_lazy('library:patent-list')
    template_name = 'library/patent/patent_create_form.html'
    form_class = PatentModelForm
    extra_context = {'title': 'Добавить патент'}


class PatentUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Patent
    form_class = PatentModelForm
    success_url = reverse_lazy('library:patent-list')
    template_name = 'library/patent/patent_create_form.html'
    extra_context = {'title': 'Изменить патент'}


class PatentDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Patent
    context_object_name = 'patent'
    slug_field = 'slug'
    success_url = reverse_lazy('library:patent-list')
    extra_context = {'title': 'Удалить патент'}
