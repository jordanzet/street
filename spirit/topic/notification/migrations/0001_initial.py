# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_comment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spirit_topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('action', models.IntegerField(default=0, choices=[(0, 'Undefined'), (1, 'Mention'), (2, 'Comment')])),
                ('is_read', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(to='spirit_comment.Comment')),
                ('topic', models.ForeignKey(to='spirit_topic.Topic')),
                ('user', models.ForeignKey(related_name='st_topic_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date', '-pk'],
                'verbose_name': 'topic notification',
                'verbose_name_plural': 'topics notification',
            },
        ),
        migrations.AlterUniqueTogether(
            name='topicnotification',
            unique_together=set([('user', 'topic')]),
        ),
    ]
