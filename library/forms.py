from crispy_bootstrap5.bootstrap5 import Switch
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from library.models import (Abstract, Textbook, Program, Patent, InnovationProposal,
                            Monograph, Dissertation, Article, Author, Review)
from django.forms.widgets import DateInput, ClearableFileInput


class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class ReviewFieldFormMixin(forms.ModelForm):
    reviews = MultipleFileField(required=False, label='Файлы рецензий')


class BaseModelHelperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn btn-success'))


class BaseModelForm(BaseModelHelperForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), required=True, label='Авторы')
    exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.get('initial', {})
            initial['authors'] = [a.pk for a in kwargs['instance'].authors.all()]

        super().__init__(*args, **kwargs)
        self.fields['annotation'].widget.attrs["rows"] = 5
        self.helper['is_secret'].wrap(Switch)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self)
        instance.authors.clear()
        instance.authors.add(*self.cleaned_data['authors'])
        return instance

    class Meta:
        widgets = {
            "publication_date": DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class AuthorModelForm(BaseModelHelperForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "patronymic", 'division', "rank", 'user', "science_works"]


class AbstractModelForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Abstract
        fields = ["name", "annotation", "is_secret", "udc", "publication_date", "file", "conclusion_file"]


class TextbookModelForm(BaseModelForm, ReviewFieldFormMixin):
    class Meta(BaseModelForm.Meta):
        model = Textbook
        fields = ["name", "annotation", "is_secret", "isbn", "udc", "publication_date",
                  "file", "STC_certificate", "conclusion_file", 'authors', 'reviews']


class ProgramModelForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Program
        fields = ["name", "annotation", "is_secret", "doc_num", "publication_date",
                  "file", "implementation_act", "conclusion_file"]


class PatentModelForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = Patent
        fields = ["name", "annotation", "is_secret", 'patent_type', 'patent_owner', "doc_num", "publication_date",
                  "file", "implementation_act", "conclusion_file"]


class ProposalModelForm(BaseModelForm):
    class Meta(BaseModelForm.Meta):
        model = InnovationProposal
        fields = ["name", "annotation", "is_secret", "doc_num", "publication_date",
                  "file", "implementation_act", 'certificate', "conclusion_file"]


class MonographModelForm(BaseModelForm, ReviewFieldFormMixin):
    class Meta(BaseModelForm.Meta):
        model = Monograph
        fields = ["name", "annotation", "is_secret", "isbn", "udc", "publication_date",
                  "file", "conclusion_file", 'authors', 'reviews']


class DissertationModelForm(BaseModelForm, ReviewFieldFormMixin):
    class Meta(BaseModelForm.Meta):
        model = Dissertation
        fields = ["name", "annotation", "is_secret", "udc", "publication_date",
                  "file", "conclusion_file", 'authors', 'reviews']


class ArticleModelForm(BaseModelForm, ReviewFieldFormMixin):
    class Meta(BaseModelForm.Meta):
        model = Article
        fields = ["name", "annotation", "is_secret", 'keywords', "science_base", 'journal',
                  "udc", "publication_date", "file", "conclusion_file", 'authors', 'reviews']


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
