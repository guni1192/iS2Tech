# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_is_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
