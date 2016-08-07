# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_topic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicPrivate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('topic', models.ForeignKey(related_name='topics_private', to='spirit_topic.Topic')),
                ('user', models.ForeignKey(related_name='st_topics_private', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date', '-pk'],
                'verbose_name': 'private topic',
                'verbose_name_plural': 'private topics',
            },
        ),
        migrations.AlterUniqueTogether(
            name='topicprivate',
            unique_together=set([('user', 'topic')]),
        ),
    ]
