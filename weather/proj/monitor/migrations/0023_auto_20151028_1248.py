# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0022_auto_20151028_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='icone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
