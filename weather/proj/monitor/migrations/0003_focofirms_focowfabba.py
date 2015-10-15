# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20150928_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='FocoFIRMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataregUTC', models.DateTimeField()),
                ('posicao', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('bright', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('scan', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('track', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('dataUTC', models.DateTimeField()),
                ('satellite', models.CharField(max_length=1)),
                ('confidence', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('version', models.CharField(max_length=5)),
                ('brightT31', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('frp', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
            ],
            options={
                'ordering': ['dataUTC'],
            },
        ),
        migrations.CreateModel(
            name='FocoWFABBA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataUTC', models.DateTimeField()),
                ('dataregUTC', models.DateTimeField()),
                ('arquivo', models.CharField(max_length=100)),
                ('posicao', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('Satzen', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('PixSize', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('T4', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('T11', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('FireSize', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('Temp', models.IntegerField(default=0)),
                ('FRP', models.IntegerField(default=0)),
                ('Ecosystem', models.IntegerField(default=0)),
                ('FireFlag', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['dataUTC'],
            },
        ),
    ]
