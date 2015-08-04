# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormalStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo', models.CharField(max_length=6)),
                ('Nome', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=50)),
                ('Uf', models.CharField(max_length=2)),
                ('Altitude', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('Tmed', models.CharField(max_length=1)),
                ('Tmax', models.CharField(max_length=1)),
                ('Tmin', models.CharField(max_length=1)),
                ('TmaxAbs', models.CharField(max_length=1)),
                ('TminAbs', models.CharField(max_length=1)),
                ('Colunas4', models.CharField(max_length=1)),
                ('Colunas5', models.CharField(max_length=1)),
                ('Pres', models.CharField(max_length=1)),
                ('Inso', models.CharField(max_length=1)),
                ('Evap', models.CharField(max_length=1)),
                ('Neb', models.CharField(max_length=1)),
                ('NebHora', models.CharField(max_length=1)),
                ('UR', models.CharField(max_length=1)),
                ('URHora', models.CharField(max_length=1)),
                ('Prec', models.CharField(max_length=1)),
                ('PrecMax', models.CharField(max_length=1)),
                ('PrecNDias', models.CharField(max_length=1)),
                ('PDec', models.CharField(max_length=1)),
                ('PdecND', models.CharField(max_length=1)),
                ('NPSec', models.CharField(max_length=2)),
                ('VentoInt', models.CharField(max_length=1)),
                ('Ventou', models.CharField(max_length=1)),
                ('Ventov', models.CharField(max_length=1)),
                ('VentoDirRes', models.CharField(max_length=1)),
                ('VentoDirPred', models.CharField(max_length=1)),
                ('NNormais', models.IntegerField(default=0)),
                ('LatLong', models.CharField(max_length=100)),
            ],
        ),
    ]
