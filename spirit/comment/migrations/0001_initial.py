# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spirit_topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='comment')),
                ('dual', models.CharField(default='mechupaunhuevo', max_length=12, choices=[('AGREE', 'de acuerdo'), ('DISAGREE', 'en desacuerdo')])),
                ('comment_html', models.TextField(verbose_name='comment html')),
                ('action', models.IntegerField(default=0, verbose_name='action', choices=[(0, 'comment'), (1, 'topic moved'), (2, 'topic closed'), (3, 'topic unclosed'), (4, 'topic pinned'), (5, 'topic unpinned')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_removed', models.BooleanField(default=False)),
                ('is_modified', models.BooleanField(default=False)),
                ('ip_address', models.GenericIPAddressField(null=True, blank=True)),
                ('modified_count', models.PositiveIntegerField(default=0, verbose_name='modified count')),
                ('likes_count', models.PositiveIntegerField(default=0, verbose_name='likes count')),
                ('topic', models.ForeignKey(to='spirit_topic.Topic')),
                ('user', models.ForeignKey(related_name='st_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date', '-pk'],
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
