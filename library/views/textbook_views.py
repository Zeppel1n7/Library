from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import TextbookModelForm
from library.models import Textbook, Review
from library.views import FileUploadMixin
from users.mixins import StaffRequiredMixin


class TextbookListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Textbook
    context_object_name = 'textbooks'
    ordering = ['-add_date']
    template_name = 'library/textbook/textbook_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Учебные пособия'}


class TextbookDetailView(LoginRequiredMixin, DetailView):
    model = Textbook
    context_object_name = 'textbook'
    slug_field = 'slug'
    template_name = 'library/textbook/textbook_detail.html'
    extra_context = {'title': 'Просмотр учебного пособия'}


class TextbookCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView, FileUploadMixin):
    model = Textbook
    success_url = reverse_lazy('library:textbook-list')
    template_name = 'library/textbook/textbook_create_form.html'
    form_class = TextbookModelForm
    extra_context = {'title': 'Добавить учебное пособие'}
    file_field_name = 'reviews'

    def create_related_object(self, file):
        Review.objects.create(textbook=self.object, file=file)


class TextbookUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView, FileUploadMixin):
    model = Textbook
    form_class = TextbookModelForm
    success_url = reverse_lazy('library:textbook-list')
    template_name = 'library/textbook/textbook_create_form.html'
    extra_context = {'title': 'Изменить учебное пособие'}
    file_field_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['reviews'] = Review.objects.filter(textbook=self.object).all()
        return context

    def create_related_object(self, file):
        Review.objects.create(textbook=self.object, file=file)


class TextbookDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Textbook
    context_object_name = 'textbook'
    slug_field = 'slug'
    success_url = reverse_lazy('library:textbook-list')
    extra_context = {'title': 'Удалить учебное пособие'}
