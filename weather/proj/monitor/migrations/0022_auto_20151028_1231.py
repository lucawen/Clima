# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0021_kpi_kpi_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi_nivel',
            name='KPI_FK',
            field=models.ForeignKey(verbose_name=b'KPI', to='monitor.KPI'),
        ),
    ]
