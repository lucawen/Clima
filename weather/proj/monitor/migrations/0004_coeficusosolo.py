# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_focofirms_focowfabba'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoeficUsoSolo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usosolo', models.CharField(max_length=100, verbose_name=b'Categoria    de Uso')),
                ('coefic', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('Projeto_FK', models.ForeignKey(verbose_name=b'Projeto', to='monitor.Projeto')),
            ],
        ),
    ]
