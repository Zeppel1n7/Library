from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import AuthorModelForm
from library.models import Author
from users.mixins import StaffRequiredMixin


class AuthorListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Author
    context_object_name = 'authors'
    ordering = ['-last_name']
    template_name = 'library/author/author_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Авторы'}


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'library/author/author_detail.html'
    extra_context = {'title': 'Просмотр автора'}


class AuthorCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy('library:author-list')
    template_name = 'library/author/author_create_form.html'
    form_class = AuthorModelForm
    extra_context = {'title': 'Добавить автора'}


class AuthorUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorModelForm
    success_url = reverse_lazy('library:author-list')
    template_name = 'library/author/author_create_form.html'
    extra_context = {'title': 'Изменить автора'}


class AuthorDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Author
    context_object_name = 'author'
    success_url = reverse_lazy('library:author-list')
    extra_context = {'title': 'Удалить автора'}
