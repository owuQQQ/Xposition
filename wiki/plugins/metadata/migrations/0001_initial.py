# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-02 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wiki', '0009_auto_20170426_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('revisionplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wiki.RevisionPlugin')),
            ],
            options={
                'verbose_name': 'metadata',
            },
            bases=('wiki.revisionplugin',),
        ),
        migrations.CreateModel(
            name='MetadataRevision',
            fields=[
                ('revisionpluginrevision_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='wiki.RevisionPluginRevision')),
                ('template', models.CharField(default='wiki/view.html', editable=False, max_length=100)),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'metadata revision',
            },
            bases=('wiki.revisionpluginrevision',),
        ),
        migrations.CreateModel(
            name='Supersense',
            fields=[
                ('metadata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metadata.Metadata')),
            ],
            options={
                'verbose_name': 'supersense',
            },
            bases=('metadata.metadata',),
        ),
        migrations.CreateModel(
            name='SupersenseRevision',
            fields=[
                ('metadatarevision_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metadata.MetadataRevision')),
                ('animacy', models.DecimalField(decimal_places=0, max_digits=2)),
                ('counterpart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metadata.SupersenseRevision')),
            ],
            options={
                'verbose_name': 'supersense revision',
            },
            bases=('metadata.metadatarevision',),
        ),
        migrations.AddField(
            model_name='metadatarevision',
            name='article',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.Article'),
        ),
    ]
