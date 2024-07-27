from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import AbstractModelForm
from library.models import Abstract
from users.mixins import StaffRequiredMixin


class AbstractListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Abstract
    context_object_name = 'abstracts'
    ordering = ['-add_date']
    template_name = 'library/abstract/abstract_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Авторефераты'}


class AbstractDetailView(LoginRequiredMixin, DetailView):
    model = Abstract
    context_object_name = 'abstract'
    slug_field = 'slug'
    template_name = 'library/abstract/abstract_detail.html'
    extra_context = {'title': 'Просмотр автореферата'}


class AbstractCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Abstract
    success_url = reverse_lazy('library:abstract-list')
    template_name = 'library/abstract/abstract_create_form.html'
    form_class = AbstractModelForm
    extra_context = {'title': 'Добавить автореферат'}


class AbstractUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Abstract
    form_class = AbstractModelForm
    success_url = reverse_lazy('library:abstract-list')
    template_name = 'library/abstract/abstract_create_form.html'
    extra_context = {'title': 'Изменить автореферат'}


class AbstractDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Abstract
    context_object_name = 'abstract'
    slug_field = 'slug'
    success_url = reverse_lazy('library:abstract-list')
    extra_context = {'title': 'Удалить автореферат'}
