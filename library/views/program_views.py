from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import ProgramModelForm
from library.models import Program
from users.mixins import StaffRequiredMixin


class ProgramListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Program
    context_object_name = 'programs'
    ordering = ['-add_date']
    template_name = 'library/program/program_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Программы для ЭВМ'}


class ProgramDetailView(LoginRequiredMixin, DetailView):
    model = Program
    context_object_name = 'program'
    slug_field = 'slug'
    template_name = 'library/program/program_detail.html'
    extra_context = {'title': 'Просмотр ПЭВМ'}


class ProgramCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Program
    success_url = reverse_lazy('library:program-list')
    template_name = 'library/program/program_create_form.html'
    form_class = ProgramModelForm
    extra_context = {'title': 'Добавить программу для ЭВМ'}


class ProgramUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramModelForm
    success_url = reverse_lazy('library:program-list')
    template_name = 'library/program/program_create_form.html'
    extra_context = {'title': 'Изменить программу для ЭВМ'}


class ProgramDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Program
    context_object_name = 'program'
    slug_field = 'slug'
    success_url = reverse_lazy('library:program-list')
    extra_context = {'title': 'Удалить ПЭВМ'}
