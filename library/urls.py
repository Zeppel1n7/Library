from django.urls import path, include
from . import views

app_name = 'library'

abstract_patterns = [
    path('', views.AbstractListView.as_view(), name='abstract-list'),
    path('new/', views.AbstractCreateView.as_view(), name='abstract-create'),
    path('<slug:slug>/', views.AbstractDetailView.as_view(), name='abstract-detail'),
    path('<slug:slug>/update', views.AbstractUpdateView.as_view(), name='abstract-update'),
    path('<slug:slug>/delete', views.AbstractDeleteView.as_view(), name='abstract-delete'),
]

article_patterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('new/', views.ArticleCreateView.as_view(), name='article-create'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('<slug:slug>/update', views.ArticleUpdateView.as_view(), name='article-update'),
    path('<slug:slug>/delete', views.ArticleDeleteView.as_view(), name='article-delete'),
]

dissertation_patterns = [
    path('', views.DissertationListView.as_view(), name='dissertation-list'),
    path('new/', views.DissertationCreateView.as_view(), name='dissertation-create'),
    path('<slug:slug>/', views.DissertationDetailView.as_view(), name='dissertation-detail'),
    path('<slug:slug>/update', views.DissertationUpdateView.as_view(), name='dissertation-update'),
    path('<slug:slug>/delete', views.DissertationDeleteView.as_view(), name='dissertation-delete'),
]

proposal_patterns = [
    path('', views.ProposalListView.as_view(), name='proposal-list'),
    path('new/', views.ProposalCreateView.as_view(), name='proposal-create'),
    path('<slug:slug>/', views.ProposalDetailView.as_view(), name='proposal-detail'),
    path('<slug:slug>/update', views.ProposalUpdateView.as_view(), name='proposal-update'),
    path('<slug:slug>/delete', views.ProposalDeleteView.as_view(), name='proposal-delete'),
]

monograph_patterns = [
    path('', views.MonographListView.as_view(), name='monograph-list'),
    path('new/', views.MonographCreateView.as_view(), name='monograph-create'),
    path('<slug:slug>/', views.MonographDetailView.as_view(), name='monograph-detail'),
    path('<slug:slug>/update', views.MonographUpdateView.as_view(), name='monograph-update'),
    path('<slug:slug>/delete', views.MonographDeleteView.as_view(), name='monograph-delete'),
]

patent_patterns = [
    path('', views.PatentListView.as_view(), name='patent-list'),
    path('new/', views.PatentCreateView.as_view(), name='patent-create'),
    path('<slug:slug>/', views.PatentDetailView.as_view(), name='patent-detail'),
    path('<slug:slug>/update', views.PatentUpdateView.as_view(), name='patent-update'),
    path('<slug:slug>/delete', views.PatentDeleteView.as_view(), name='patent-delete'),
]

program_patterns = [
    path('', views.ProgramListView.as_view(), name='program-list'),
    path('new/', views.ProgramCreateView.as_view(), name='program-create'),
    path('<slug:slug>/', views.ProgramDetailView.as_view(), name='program-detail'),
    path('<slug:slug>/update', views.ProgramUpdateView.as_view(), name='program-update'),
    path('<slug:slug>/delete', views.ProgramDeleteView.as_view(), name='program-delete'),
]

textbook_patterns = [
    path('', views.TextbookListView.as_view(), name='textbook-list'),
    path('new/', views.TextbookCreateView.as_view(), name='textbook-create'),
    path('<slug:slug>/', views.TextbookDetailView.as_view(), name='textbook-detail'),
    path('<slug:slug>/update', views.TextbookUpdateView.as_view(), name='textbook-update'),
    path('<slug:slug>/delete', views.TextbookDeleteView.as_view(), name='textbook-delete'),
]

author_patterns = [
    path('', views.AuthorListView.as_view(), name='author-list'),
    path('new/', views.AuthorCreateView.as_view(), name='author-create'),
    path('<uuid:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('<uuid:pk>/update', views.AuthorUpdateView.as_view(), name='author-update'),
    path('<uuid:pk>/delete', views.AuthorDeleteView.as_view(), name='author-delete'),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('author/', include(author_patterns)),
    path('abstract/', include(abstract_patterns)),
    path('article/', include(article_patterns)),
    path('dissertation/', include(dissertation_patterns)),
    path('proposal/', include(proposal_patterns)),
    path('monograph/', include(monograph_patterns)),
    path('patent/', include(patent_patterns)),
    path('program/', include(program_patterns)),
    path('textbook/', include(textbook_patterns))
]
