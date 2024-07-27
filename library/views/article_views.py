from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import ArticleModelForm
from library.models import Article, Review
from .mixin_views import FileUploadMixin
from users.mixins import StaffRequiredMixin


class ArticleListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = Article
    context_object_name = 'articles'
    ordering = ['-add_date']
    template_name = 'library/article/article_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Научные статьи'}

    def get_queryset(self):
        qs = super(ArticleListView, self).get_queryset()
        return qs.prefetch_related('science_base')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = 'article'
    slug_field = 'slug'
    template_name = 'library/article/article_detail.html'
    extra_context = {'title': 'Просмотр статьи'}


class ArticleCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView, FileUploadMixin):
    model = Article
    success_url = reverse_lazy('library:article-list')
    template_name = 'library/article/article_create_form.html'
    form_class = ArticleModelForm
    extra_context = {'title': 'Добавить статью'}
    file_field_name = 'reviews'

    def create_related_object(self, file):
        Review.objects.create(article=self.object, file=file)


class ArticleUpdateView(LoginRequiredMixin, StaffRequiredMixin, FileUploadMixin, UpdateView):
    model = Article
    form_class = ArticleModelForm
    success_url = reverse_lazy('library:article-list')
    template_name = 'library/article/article_create_form.html'
    extra_context = {'title': 'Изменить статью'}
    file_field_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['reviews'] = Review.objects.filter(article=self.object).all()
        return context

    def create_related_object(self, file):
        Review.objects.create(article=self.object, file=file)


class ArticleDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Article
    context_object_name = 'article'
    slug_field = 'slug'
    success_url = reverse_lazy('library:article-list')
    extra_context = {'title': 'Удалить статью'}
