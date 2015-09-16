# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0008_auto_20150916_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='nome',
            field=models.CharField(unique=True, max_length=300, verbose_name=b'Parametro'),
        ),
    ]
