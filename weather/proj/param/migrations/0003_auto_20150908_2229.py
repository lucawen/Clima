# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0002_auto_20150908_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='monitorado',
            field=models.BooleanField(max_length=3, choices=[(b'0', b'NAO'), (b'1', b'SIM')]),
        ),
        migrations.AlterField(
            model_name='param',
            name='tipoParametro',
            field=models.CharField(max_length=1, choices=[(b'0', b'valor'), (b'1', b'texto'), (b'2', b'imagem'), (b'3', b'classe'), (b'4', b'calculado')]),
        ),
    ]
