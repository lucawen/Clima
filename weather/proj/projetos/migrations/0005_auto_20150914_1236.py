# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0004_auto_20150914_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midia',
            name='Medicao_FK',
            field=models.ForeignKey(verbose_name=b'Medicao', to='projetos.Medicao'),
        ),
        migrations.AlterField(
            model_name='texto',
            name='Medicao_FK',
            field=models.ForeignKey(verbose_name=b'Medicao', to='projetos.Medicao'),
        ),
    ]
