# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 05:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20170819_0708'),
        ('metadata', 'construal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('metadata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metadata.Metadata')),
            ],
            options={
                'verbose_name': 'corpus',
            },
            bases=('metadata.metadata',),
        ),

        migrations.CreateModel(
            name='ExampleRevision',
            fields=[
                ('metadatarevision_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metadata.MetadataRevision')),
                ('exampleXML', models.CharField(max_length=200)),
                ('usage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='metadata.Construal')),
            ],
            options={
                'verbose_name': 'example revision',
            },
            bases=('metadata.metadatarevision',),
        ),
    ]
