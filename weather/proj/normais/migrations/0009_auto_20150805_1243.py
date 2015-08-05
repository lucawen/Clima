# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0008_resultstr'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametro',
            name='tipoMapa',
            field=models.CharField(default=b'', max_length=2, blank=True),
        ),
        migrations.AddField(
            model_name='parametro',
            name='unidade',
            field=models.CharField(default=b'', max_length=15, blank=True),
        ),
    ]
