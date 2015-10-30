# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0020_auto_20151023_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordem', models.IntegerField(default=0)),
                ('nome', models.CharField(max_length=6)),
                ('unidade', models.CharField(max_length=6)),
                ('icone', models.CharField(max_length=6)),
                ('msg', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ['ordem'],
            },
        ),
        migrations.CreateModel(
            name='KPI_Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v1', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('v2', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('texto', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=10)),
                ('KPI_FK', models.ForeignKey(verbose_name=b'KPI', to='monitor.Alarme')),
            ],
            options={
                'ordering': ['KPI_FK', 'v1'],
            },
        ),
    ]
