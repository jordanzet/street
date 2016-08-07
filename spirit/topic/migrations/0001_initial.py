# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import spirit.core.utils.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spirit_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', spirit.core.utils.models.AutoSlugField(db_index=False, populate_from='title', blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('last_active', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last active')),
                ('reindex_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='reindex at')),
                ('is_pinned', models.BooleanField(default=False, verbose_name='pinned')),
                ('is_globally_pinned', models.BooleanField(default=False, verbose_name='globally pinned')),
                ('is_closed', models.BooleanField(default=False, verbose_name='closed')),
                ('is_removed', models.BooleanField(default=False)),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='views count')),
                ('comment_count', models.PositiveIntegerField(default=0, verbose_name='comment count')),
                ('category', models.ForeignKey(verbose_name='category', to='spirit_category.Category')),
                ('user', models.ForeignKey(related_name='st_topics', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-last_active', '-pk'],
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
        ),
    ]
