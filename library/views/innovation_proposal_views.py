from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from EraLibrary import settings
from library.forms import ProposalModelForm
from library.models import InnovationProposal
from users.mixins import StaffRequiredMixin


class ProposalListView(LoginRequiredMixin, ListView):
    allow_empty = True
    model = InnovationProposal
    context_object_name = 'proposals'
    ordering = ['-add_date']
    template_name = 'library/proposal/proposal_list.html'
    page_kwarg = 'page'
    paginate_by = settings.OBJ_PER_PAGE
    extra_context = {'title': 'Рацпредложения'}


class ProposalDetailView(LoginRequiredMixin, DetailView):
    model = InnovationProposal
    context_object_name = 'proposal'
    slug_field = 'slug'
    template_name = 'library/proposal/proposal_detail.html'
    extra_context = {'title': 'Просмотр рацпредложения'}


class ProposalCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = InnovationProposal
    success_url = reverse_lazy('library:proposal-list')
    template_name = 'library/proposal/proposal_create_form.html'
    form_class = ProposalModelForm
    extra_context = {'title': 'Добавить рацпредложение'}


class ProposalUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = InnovationProposal
    form_class = ProposalModelForm
    success_url = reverse_lazy('library:proposal-list')
    template_name = 'library/proposal/proposal_create_form.html'
    extra_context = {'title': 'Изменить рацпредложение'}


class ProposalDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = InnovationProposal
    context_object_name = 'proposal'
    slug_field = 'slug'
    success_url = reverse_lazy('library:proposal-list')
    extra_context = {'title': 'Удалить рацпредложение'}
