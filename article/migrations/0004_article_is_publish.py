# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_article_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]