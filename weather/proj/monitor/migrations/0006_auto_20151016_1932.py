# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_coeficusosolo_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coeficusosolo',
            name='Projeto_FK',
        ),
        migrations.AddField(
            model_name='camada',
            name='coefic',
            field=models.DecimalField(default=0, max_digits=16, decimal_places=2),
        ),
        migrations.DeleteModel(
            name='CoeficUsoSolo',
        ),
    ]
