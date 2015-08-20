# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0002_station_posicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='Evap',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Inso',
        ),
        migrations.RemoveField(
            model_name='station',
            name='NNormais',
        ),
        migrations.RemoveField(
            model_name='station',
            name='NPSec',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Neb',
        ),
        migrations.RemoveField(
            model_name='station',
            name='NebHora',
        ),
        migrations.RemoveField(
            model_name='station',
            name='PDec',
        ),
        migrations.RemoveField(
            model_name='station',
            name='PdecND',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Prec',
        ),
        migrations.RemoveField(
            model_name='station',
            name='PrecMax',
        ),
        migrations.RemoveField(
            model_name='station',
            name='PrecNDias',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Pres',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Tmax',
        ),
        migrations.RemoveField(
            model_name='station',
            name='TmaxAbs',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Tmed',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Tmin',
        ),
        migrations.RemoveField(
            model_name='station',
            name='TminAbs',
        ),
        migrations.RemoveField(
            model_name='station',
            name='UR',
        ),
        migrations.RemoveField(
            model_name='station',
            name='URHora',
        ),
        migrations.RemoveField(
            model_name='station',
            name='VentoDirPred',
        ),
        migrations.RemoveField(
            model_name='station',
            name='VentoDirRes',
        ),
        migrations.RemoveField(
            model_name='station',
            name='VentoInt',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Ventou',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Ventov',
        ),
        migrations.AddField(
            model_name='station',
            name='tipo',
            field=models.CharField(default=b'N', max_length=1),
        ),
    ]
