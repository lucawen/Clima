# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0012_alarme_figura'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAlarme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alg', models.CharField(max_length=6)),
                ('foco_id', models.IntegerField(default=0)),
                ('dataUTC', models.DateTimeField()),
                ('dataregUTC', models.DateTimeField()),
                ('posicao', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('temp', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('satellite', models.CharField(max_length=10)),
                ('pixsize', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
                ('fireSize', models.DecimalField(default=0, max_digits=16, decimal_places=4)),
            ],
        ),
        migrations.RenameField(
            model_name='focofirms',
            old_name='confidence',
            new_name='yyconfidence',
        ),
        migrations.RemoveField(
            model_name='alarme',
            name='algoritimo',
        ),
        migrations.RemoveField(
            model_name='alarme',
            name='figura',
        ),
        migrations.RemoveField(
            model_name='alarme',
            name='foco_id',
        ),
        migrations.AddField(
            model_name='itemalarme',
            name='Alarme_FK',
            field=models.ForeignKey(verbose_name=b'Alarme', to='monitor.Alarme'),
        ),
    ]
