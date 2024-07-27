from django.utils.crypto import get_random_string
from django.utils.text import slugify
from unidecode import unidecode


def unique_slugify(instance, text_ref, max_length=10, slug_field='slug'):
    slug_field_max_length = instance._meta.get_field(slug_field).max_length
    if not max_length or max_length > slug_field_max_length:
        max_length = slug_field_max_length

    unique_slug = slug = slugify(unidecode(text_ref))[:max_length]

    model = instance.__class__
    while model.objects.filter(slug=unique_slug).exists():
        if len(slug) + 9 > max_length:
            slug = slug[:max_length - 9]
        unique_slug = f'{slug}-{get_random_string(length=8)}'

    return unique_slug
