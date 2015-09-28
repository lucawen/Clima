# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pontos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upgrh', models.CharField(max_length=150)),
                ('estacao', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=150)),
                ('classeEnquad', models.CharField(max_length=150)),
                ('datEstab', models.DateField()),
                ('datDesatBac', models.DateField()),
                ('Bacia', models.CharField(max_length=150)),
                ('SubBacia', models.CharField(max_length=150)),
                ('CursoDAgua', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('municipio', models.CharField(max_length=150)),
                ('altitude', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('tipoCorpDAgua', models.CharField(max_length=150)),
                ('posicao', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
    ]
