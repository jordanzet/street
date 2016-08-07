# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import spirit.core.utils.models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-date_joined', '-pk'],
                'abstract': False,
                'verbose_name_plural': 'users',
                'db_table': 'spirit_user_user',
                'verbose_name': 'user',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', spirit.core.utils.models.AutoSlugField(db_index=False, populate_from='user.username', blank=True)),
                ('location', models.CharField(max_length=75, verbose_name='location', blank=True)),
                ('last_seen', models.DateTimeField(auto_now=True, verbose_name='last seen')),
                ('last_ip', models.GenericIPAddressField(null=True, verbose_name='last ip', blank=True)),
                ('timezone', models.CharField(default='UTC-0500', max_length=32, verbose_name='time zone')),
                ('image_profile', models.ImageField(null=True, upload_to='userprofile/image/', blank=True)),
                ('is_administrator', models.BooleanField(default=False, verbose_name='administrator status')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='moderator status')),
                ('is_verified', models.BooleanField(default=False, help_text='Designates whether the user has verified his account by email or by other means. Un-select this to let the user activate his account.', verbose_name='verified')),
                ('topic_count', models.PositiveIntegerField(default=0, verbose_name='topic count')),
                ('comment_count', models.PositiveIntegerField(default=0, verbose_name='comment count')),
                ('last_post_hash', models.CharField(max_length=32, verbose_name='last post hash', blank=True)),
                ('last_post_on', models.DateTimeField(null=True, verbose_name='last post on', blank=True)),
                ('user', models.OneToOneField(related_name='st', verbose_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'forum profile',
                'verbose_name_plural': 'forum profiles',
            },
        ),
    ]
