from django import template
from pathlib import Path

from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def filename(value):
    return Path(value).name
