# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(default=0)),
                ('Nome', models.CharField(max_length=100)),
                ('Planilha', models.CharField(default=b'', max_length=200)),
                ('jan', models.IntegerField(default=0)),
                ('fev', models.IntegerField(default=0)),
                ('mar', models.IntegerField(default=0)),
                ('abr', models.IntegerField(default=0)),
                ('mai', models.IntegerField(default=0)),
                ('jun', models.IntegerField(default=0)),
                ('jul', models.IntegerField(default=0)),
                ('ago', models.IntegerField(default=0)),
                ('stb', models.IntegerField(default=0)),
                ('out', models.IntegerField(default=0)),
                ('nov', models.IntegerField(default=0)),
                ('dez', models.IntegerField(default=0)),
                ('tot', models.IntegerField(default=0)),
                ('unidade', models.CharField(default=b'', max_length=15, blank=True)),
                ('Classe_FK', models.ForeignKey(default=None, blank=True, to='normais.Classe', null=True, verbose_name=b'Classe')),
            ],
            options={
                'ordering': ['Nome'],
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jan', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('fev', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('mar', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('abr', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('mai', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('jun', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('jul', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('ago', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('stb', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('out', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('nov', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('dez', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('tot', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('Parametro_FK', models.ForeignKey(verbose_name=b'Par\xc3\xa2metro', to='normais.Parametro')),
            ],
        ),
        migrations.CreateModel(
            name='ResultStr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jan', models.CharField(default=b'', max_length=20)),
                ('fev', models.CharField(default=b'', max_length=20)),
                ('mar', models.CharField(default=b'', max_length=20)),
                ('abr', models.CharField(default=b'', max_length=20)),
                ('mai', models.CharField(default=b'', max_length=20)),
                ('jun', models.CharField(default=b'', max_length=20)),
                ('jul', models.CharField(default=b'', max_length=20)),
                ('ago', models.CharField(default=b'', max_length=20)),
                ('stb', models.CharField(default=b'', max_length=20)),
                ('out', models.CharField(default=b'', max_length=20)),
                ('nov', models.CharField(default=b'', max_length=20)),
                ('dez', models.CharField(default=b'', max_length=20)),
                ('tot', models.CharField(default=b'', max_length=20)),
                ('Parametro_FK', models.ForeignKey(verbose_name=b'Par\xc3\xa2metro', to='normais.Parametro')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo', models.CharField(max_length=6)),
                ('Nome', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=50)),
                ('UF', models.CharField(max_length=2)),
                ('Altitude', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('Tmed', models.CharField(max_length=1)),
                ('Tmax', models.CharField(max_length=1)),
                ('Tmin', models.CharField(max_length=1)),
                ('TmaxAbs', models.CharField(max_length=1)),
                ('TminAbs', models.CharField(max_length=1)),
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
            options={
                'ordering': ['Nome'],
            },
        ),
        migrations.AddField(
            model_name='resultstr',
            name='Station_FK',
            field=models.ForeignKey(verbose_name=b'Esta\xc3\xa7\xc3\xa3o', to='normais.Station'),
        ),
        migrations.AddField(
            model_name='resultado',
            name='Station_FK',
            field=models.ForeignKey(verbose_name=b'Esta\xc3\xa7\xc3\xa3o', to='normais.Station'),
        ),
    ]
