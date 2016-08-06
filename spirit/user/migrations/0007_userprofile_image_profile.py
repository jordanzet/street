# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_user', '0006_auto_20160606_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_profile',
            field=models.ImageField(null=True, upload_to='userprofile/image/', blank=True),
        ),
    ]
