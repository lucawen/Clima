# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0004_auto_20150908_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='nome',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
