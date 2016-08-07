# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import spirit.core.utils.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=75, verbose_name='title')),
                ('slug', spirit.core.utils.models.AutoSlugField(db_index=False, populate_from='title', blank=True)),
                ('description', models.CharField(max_length=255, verbose_name='description', blank=True)),
                ('color', models.CharField(help_text='Title color in hex format (i.e: #1aafd0).', max_length=7, verbose_name='color', blank=True)),
                ('reindex_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified at')),
                ('is_global', models.BooleanField(default=True, help_text='Designates whether the topics will bedisplayed in the all-categories list.', verbose_name='global')),
                ('is_closed', models.BooleanField(default=False, verbose_name='closed')),
                ('is_removed', models.BooleanField(default=False, verbose_name='removed')),
                ('is_private', models.BooleanField(default=False, verbose_name='private')),
                ('parent', models.ForeignKey(verbose_name='category parent', blank=True, to='spirit_category.Category', null=True)),
            ],
            options={
                'ordering': ['title', 'pk'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
