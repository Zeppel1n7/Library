# Generated by Django 5.0.6 on 2024-06-20 13:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_article_review_remove_textbook_review_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'автора', 'verbose_name_plural': 'авторы'},
        ),
        migrations.AlterField(
            model_name='sciencework',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
