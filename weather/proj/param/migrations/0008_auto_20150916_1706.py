# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0007_auto_20150910_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='param',
            options={'ordering': ['created'], 'verbose_name': 'Par\xe2metro', 'verbose_name_plural': 'Par\xe2metros'},
        ),
        migrations.AlterModelOptions(
            name='unidade',
            options={'ordering': ['sigla'], 'verbose_name': 'Unidade', 'verbose_name_plural': 'Unidades'},
        ),
        migrations.AlterField(
            model_name='param',
            name='nome',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'Parametro'),
        ),
    ]
