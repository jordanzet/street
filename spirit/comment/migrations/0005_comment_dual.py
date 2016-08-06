# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_comment', '0004_auto_20160315_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dual',
            field=models.CharField(default=datetime.datetime(2016, 7, 28, 16, 53, 31, 278411, tzinfo=utc), max_length=12, choices=[('AGREE', 'de acuerdo'), ('DISAGREE', 'en desacuerdo')]),
            preserve_default=False,
        ),
    ]
