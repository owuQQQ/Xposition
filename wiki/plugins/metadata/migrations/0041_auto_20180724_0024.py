# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-24 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0040_auto_20180723_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adpositionrevision',
            name='is_pp_idiom',
            field=models.BooleanField(default=False, verbose_name='Is PP Idiom?'),
        ),
    ]