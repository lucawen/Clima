# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0004_parametro_corgrafico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
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
                'ordering': ['data'],
            },
        ),
    ]
