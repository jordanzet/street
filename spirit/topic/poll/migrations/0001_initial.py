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
            name='TopicPoll',
            fields=[
                ('topic', models.OneToOneField(related_name='poll', primary_key=True, serialize=False, to='spirit_topic.Topic', verbose_name='topic')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('choice_limit', models.PositiveIntegerField(default=1, verbose_name='choice limit')),
                ('is_closed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'topic poll',
                'verbose_name_plural': 'topics polls',
            },
        ),
        migrations.CreateModel(
            name='TopicPollChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name='choice description')),
                ('vote_count', models.PositiveIntegerField(default=0, verbose_name='vote count')),
                ('poll', models.ForeignKey(related_name='choices', verbose_name='poll', to='spirit_topic_poll.TopicPoll')),
            ],
            options={
                'verbose_name': 'poll choice',
                'verbose_name_plural': 'poll choices',
            },
        ),
        migrations.CreateModel(
            name='TopicPollVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('choice', models.ForeignKey(related_name='votes', verbose_name='poll choice', to='spirit_topic_poll.TopicPollChoice')),
                ('user', models.ForeignKey(related_name='st_votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'poll vote',
                'verbose_name_plural': 'poll votes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='topicpollvote',
            unique_together=set([('user', 'choice')]),
        ),
    ]
