# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0019_auto_20151016_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicao',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='medicao',
            name='dataInc',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
