# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0016_medicao_vlrlbl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptomonit',
            name='nome',
            field=models.CharField(default=b'', unique=True, max_length=2200, verbose_name=b'Pto.Monit.'),
        ),
        migrations.AlterField(
            model_name='ptomonit',
            name='sigla',
            field=models.CharField(default=b'', unique=True, max_length=15, verbose_name=b'Codigo do Ponto.', db_index=True),
        ),
    ]
