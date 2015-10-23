# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0016_alarme_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarme',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 20, 9, 6, 422373)),
        ),
    ]
