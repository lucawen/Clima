# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0009_auto_20150916_2005'),
        ('projetos', '0011_auto_20150916_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ptomonit',
            name='Parametro_FK',
        ),
        migrations.AddField(
            model_name='medicao',
            name='Parametro_FK',
            field=models.ForeignKey(default=0, verbose_name=b'Parametro', to='param.Param'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ptomonit',
            name='sigla',
            field=models.CharField(default=b'', max_length=15, verbose_name=b'C\xc3digo do Ponto.'),
        ),
    ]
