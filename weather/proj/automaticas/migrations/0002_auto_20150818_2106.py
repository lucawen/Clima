# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0004_parametro_corgrafico'),
        ('automaticas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicaoDiaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(verbose_name=b'Data')),
                ('numdia', models.IntegerField(default=0, verbose_name=b'Dia')),
                ('leituras', models.IntegerField(default=0, verbose_name=b'Leiruras')),
                ('tempIns', models.DecimalField(default=0, verbose_name=b'Temp Inst', max_digits=16, decimal_places=2)),
                ('tempMax', models.DecimalField(default=0, verbose_name=b'Temp Max', max_digits=16, decimal_places=2)),
                ('tempMin', models.DecimalField(default=0, verbose_name=b'Temp Min', max_digits=16, decimal_places=2)),
                ('umidIns', models.DecimalField(default=0, verbose_name=b'Umid Inst', max_digits=16, decimal_places=2)),
                ('umidMax', models.DecimalField(default=0, verbose_name=b'Umid Max', max_digits=16, decimal_places=2)),
                ('umidMin', models.DecimalField(default=0, verbose_name=b'Umid Min', max_digits=16, decimal_places=2)),
                ('pressao', models.DecimalField(default=0, verbose_name=b'Pressao', max_digits=16, decimal_places=2)),
                ('ventoVel', models.DecimalField(default=0, verbose_name=b'Vento Vel', max_digits=16, decimal_places=2)),
                ('ventoRaj', models.DecimalField(default=0, verbose_name=b'Vento Raj', max_digits=16, decimal_places=2)),
                ('radiac', models.DecimalField(default=0, verbose_name=b'Radia\xc3\xa7\xc3\xa3o', max_digits=16, decimal_places=2)),
                ('precipt', models.DecimalField(default=0, verbose_name=b'Precipitacao', max_digits=16, decimal_places=2)),
                ('ventoN', models.DecimalField(default=0, verbose_name=b'Vento N', max_digits=16, decimal_places=2)),
                ('ventoNE', models.DecimalField(default=0, verbose_name=b'Vento NE', max_digits=16, decimal_places=2)),
                ('ventoE', models.DecimalField(default=0, verbose_name=b'Vento E', max_digits=16, decimal_places=2)),
                ('ventoSE', models.DecimalField(default=0, verbose_name=b'Vento SE', max_digits=16, decimal_places=2)),
                ('ventoS', models.DecimalField(default=0, verbose_name=b'Vento S', max_digits=16, decimal_places=2)),
                ('ventoSW', models.DecimalField(default=0, verbose_name=b'Vento SW', max_digits=16, decimal_places=2)),
                ('ventoNW', models.DecimalField(default=0, verbose_name=b'Vento NW', max_digits=16, decimal_places=2)),
                ('estac', models.ForeignKey(verbose_name=b'Esta\xc3\xa7\xc3\xa3o', to='normais.Station')),
            ],
        ),
        migrations.CreateModel(
            name='MedicaoMensal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano', models.IntegerField(default=0, verbose_name=b'Ano')),
                ('mes', models.IntegerField(default=0, verbose_name=b'Mes')),
                ('leituras', models.IntegerField(default=0, verbose_name=b'Leiruras')),
                ('tempIns', models.DecimalField(default=0, verbose_name=b'Temp Inst', max_digits=16, decimal_places=2)),
                ('tempMax', models.DecimalField(default=0, verbose_name=b'Temp Max', max_digits=16, decimal_places=2)),
                ('tempMin', models.DecimalField(default=0, verbose_name=b'Temp Min', max_digits=16, decimal_places=2)),
                ('umidIns', models.DecimalField(default=0, verbose_name=b'Umid Inst', max_digits=16, decimal_places=2)),
                ('umidMax', models.DecimalField(default=0, verbose_name=b'Umid Max', max_digits=16, decimal_places=2)),
                ('umidMin', models.DecimalField(default=0, verbose_name=b'Umid Min', max_digits=16, decimal_places=2)),
                ('pressao', models.DecimalField(default=0, verbose_name=b'Pressao', max_digits=16, decimal_places=2)),
                ('ventoVel', models.DecimalField(default=0, verbose_name=b'Vento Vel', max_digits=16, decimal_places=2)),
                ('ventoRaj', models.DecimalField(default=0, verbose_name=b'Vento Raj', max_digits=16, decimal_places=2)),
                ('radiac', models.DecimalField(default=0, verbose_name=b'Radia\xc3\xa7\xc3\xa3o', max_digits=16, decimal_places=2)),
                ('precipt', models.DecimalField(default=0, verbose_name=b'Precipitacao', max_digits=16, decimal_places=2)),
                ('ventoN', models.DecimalField(default=0, verbose_name=b'Vento N', max_digits=16, decimal_places=2)),
                ('ventoNE', models.DecimalField(default=0, verbose_name=b'Vento NE', max_digits=16, decimal_places=2)),
                ('ventoE', models.DecimalField(default=0, verbose_name=b'Vento E', max_digits=16, decimal_places=2)),
                ('ventoSE', models.DecimalField(default=0, verbose_name=b'Vento SE', max_digits=16, decimal_places=2)),
                ('ventoS', models.DecimalField(default=0, verbose_name=b'Vento S', max_digits=16, decimal_places=2)),
                ('ventoSW', models.DecimalField(default=0, verbose_name=b'Vento SW', max_digits=16, decimal_places=2)),
                ('ventoNW', models.DecimalField(default=0, verbose_name=b'Vento NW', max_digits=16, decimal_places=2)),
                ('estac', models.ForeignKey(verbose_name=b'Esta\xc3\xa7\xc3\xa3o', to='normais.Station')),
            ],
        ),
        migrations.RemoveField(
            model_name='medicaoautomatica',
            name='estac',
        ),
        migrations.DeleteModel(
            name='MedicaoAutomatica',
        ),
    ]
