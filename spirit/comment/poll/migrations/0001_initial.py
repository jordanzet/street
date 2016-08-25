# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_comment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('choice_min', models.PositiveIntegerField(default=1, verbose_name='choice min')),
                ('choice_max', models.PositiveIntegerField(default=1, verbose_name='choice max')),
                ('mode', models.IntegerField(default=0, verbose_name='mode', choices=[(0, 'default'), (1, 'secret')])),
                ('close_at', models.DateTimeField(null=True, verbose_name='auto close at', blank=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(related_name='comment_polls', to='spirit_comment.Comment')),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name': 'comment poll',
                'verbose_name_plural': 'comments polls',
            },
        ),
        migrations.CreateModel(
            name='CommentPollChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('description', models.CharField(max_length=255, verbose_name='choice description')),
                ('vote_count', models.PositiveIntegerField(default=0, verbose_name='vote count')),
                ('is_removed', models.BooleanField(default=False)),
                ('poll', models.ForeignKey(related_name='poll_choices', to='spirit_comment_poll.CommentPoll')),
            ],
            options={
                'ordering': ['number', '-pk'],
                'verbose_name': 'poll choice',
                'verbose_name_plural': 'poll choices',
            },
        ),
        migrations.CreateModel(
            name='CommentPollVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('choice', models.ForeignKey(related_name='choice_votes', to='spirit_comment_poll.CommentPollChoice')),
                ('voter', models.ForeignKey(related_name='st_cp_votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name': 'poll vote',
                'verbose_name_plural': 'poll votes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='commentpollvote',
            unique_together=set([('voter', 'choice')]),
        ),
        migrations.AlterUniqueTogether(
            name='commentpollchoice',
            unique_together=set([('poll', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='commentpoll',
            unique_together=set([('comment', 'name')]),
        ),
    ]
