# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0005_auto_20150910_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='param',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 14, 54, 59, 899057, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
