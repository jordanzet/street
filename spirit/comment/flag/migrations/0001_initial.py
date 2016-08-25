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
            name='CommentFlag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_closed', models.BooleanField(default=False)),
                ('comment', models.OneToOneField(to='spirit_comment.Comment')),
                ('moderator', models.ForeignKey(related_name='st_comment_flags', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-date', '-pk'],
                'verbose_name': 'comment flag',
                'verbose_name_plural': 'comments flags',
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reason', models.IntegerField(verbose_name='reason', choices=[(0, 'Spam'), (1, 'Other')])),
                ('body', models.TextField(verbose_name='body', blank=True)),
                ('comment', models.ForeignKey(to='spirit_comment.Comment')),
                ('user', models.ForeignKey(related_name='st_flags', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date', '-pk'],
                'verbose_name': 'flag',
                'verbose_name_plural': 'flags',
            },
        ),
        migrations.AlterUniqueTogether(
            name='flag',
            unique_together=set([('user', 'comment')]),
        ),
    ]
