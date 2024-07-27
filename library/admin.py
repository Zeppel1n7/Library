from django.contrib import admin
from library.models import (Monograph, Abstract, Dissertation, Article, Program,
                            InnovationProposal, Patent, Textbook, ScienceBase, Author, Review, ScienceWork)
from users.admin import admin_site


class AuthorsListInline(admin.StackedInline):
    verbose_name = 'автор работы'
    verbose_name_plural = 'Авторы работы'
    extra = 1
    min_num = 1
    model = Author.science_works.through
    model._meta.local_fields[1].verbose_name = 'Автор'

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj=None, **kwargs)
        formset.validate_min = True
        return formset


class AbstractScienceWorkAdmin(admin.ModelAdmin):
    empty_value_display = "---"
    prepopulated_fields = {"slug": ["name"]}
    inlines = [AuthorsListInline]


class ReviewArticleInline(admin.StackedInline):
    model = Review
    extra = 1
    exclude = ["textbook"]


class ReviewTextbookInline(admin.StackedInline):
    model = Review
    extra = 1
    exclude = ["article"]


class AuthorAdmin(admin.ModelAdmin):
    def works_count(self, obj):
        return obj.science_works.count()

    works_count.short_description = "Количество работ"
    list_display = ["__str__", "rank", "last_name",  "first_name", "patronymic", "division", 'works_count']


class ReviewAdmin(admin.ModelAdmin):
    pass


class ScienceBaseAdmin(admin.ModelAdmin):
    pass


class ScienceWorkAdmin(AbstractScienceWorkAdmin):
    pass


class MonographAdmin(AbstractScienceWorkAdmin):
    list_display = ["__str__", "name", 'isbn', "udc", 'file', "publication_date", "add_date", "is_secret"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "udc", 'isbn',
                           "publication_date", "file", "conclusion_file", 'slug'],
            },
        )
    ]


class AbstractAdmin(AbstractScienceWorkAdmin):
    list_display = ["__str__", "name", "udc", 'file', "publication_date", "add_date", "is_secret"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "udc",
                           "publication_date", "file", "conclusion_file", 'slug'],
            },
        )
    ]


class DissertationAdmin(AbstractScienceWorkAdmin):
    list_display = ["__str__", "name", "udc", 'file', "publication_date", "add_date", "is_secret"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "udc",
                           "publication_date", "file", "conclusion_file", 'slug'],
            },
        )
    ]


class ArticleAdmin(AbstractScienceWorkAdmin):
    inlines = [*AbstractScienceWorkAdmin.inlines, ReviewArticleInline]
    list_display = ["__str__", "science_base", "name", "udc", "journal",
                    'file', "publication_date", "add_date", "is_secret"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "keywords", "science_base", "journal",
                           "udc", "publication_date", "file", "conclusion_file", 'slug'],
            },
        )
    ]


class ProgramAdmin(AbstractScienceWorkAdmin):
    list_display = ["__str__", "name", "doc_num", 'file', "publication_date", "add_date", "is_secret"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "doc_num", "publication_date",
                           "file", "implementation_act", "conclusion_file", 'slug'],
            },
        )
    ]


class InnovationProposalAdmin(AbstractScienceWorkAdmin):
    list_display = ["__str__", "name", "doc_num", 'file', "certificate", "publication_date", "add_date", "is_secret"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "doc_num", "publication_date",
                           "file", "certificate", "implementation_act", "conclusion_file", 'slug'],
            },
        )
    ]


class PatentAdmin(AbstractScienceWorkAdmin):
    list_display = ["__str__", "patent_type", "name", "doc_num", "patent_owner",
                    'file', "publication_date", "add_date", "is_secret"]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "patent_type", "patent_owner", "doc_num",
                           "publication_date", "file", "implementation_act", "conclusion_file", 'slug'],
            },
        )
    ]


class TextbookAdmin(AbstractScienceWorkAdmin):
    list_display = ["__str__", "name", 'isbn', "udc", 'file', "publication_date", "add_date", "is_secret"]
    inlines = [*AbstractScienceWorkAdmin.inlines, ReviewTextbookInline]
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "annotation", "is_secret", "isbn", "udc",
                           "publication_date", "file", "STC_certificate", "conclusion_file", 'slug'],
            },
        )
    ]


admin_site.register(Monograph, MonographAdmin)
admin_site.register(Abstract, AbstractAdmin)
admin_site.register(Dissertation, DissertationAdmin)
admin_site.register(Article, ArticleAdmin)
admin_site.register(Program, ProgramAdmin)
admin_site.register(InnovationProposal, InnovationProposalAdmin)
admin_site.register(Patent, PatentAdmin)
admin_site.register(Textbook, TextbookAdmin)
admin_site.register(ScienceBase, ScienceBaseAdmin)
admin_site.register(Author, AuthorAdmin)
admin_site.register(Review, ReviewAdmin)
# admin_site.register(ScienceWork, ScienceWorkAdmin)
