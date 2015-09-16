# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0012_auto_20150916_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptomonit',
            name='sigla',
            field=models.CharField(default=b'', max_length=15, verbose_name=b'Codigo do Ponto.'),
        ),
    ]
