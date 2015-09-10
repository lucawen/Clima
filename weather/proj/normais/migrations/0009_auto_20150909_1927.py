# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0008_auto_20150908_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foco',
            name='dataUTC',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='foco',
            name='dataregUTC',
            field=models.DateTimeField(),
        ),
    ]
