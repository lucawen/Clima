# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0015_auto_20151022_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarme',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 20, 8, 44, 211215)),
        ),
    ]
