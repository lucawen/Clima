# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0005_foco'),
    ]

    operations = [
        migrations.CreateModel(
            name='FocoiItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('foco_FK', models.ForeignKey(verbose_name=b'Foco', to='normais.Station')),
            ],
        ),
        migrations.AlterModelOptions(
            name='foco',
            options={'ordering': ['dataUTC']},
        ),
        migrations.RenameField(
            model_name='foco',
            old_name='data',
            new_name='dataUTC',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='Ecosystem',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='FRP',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='FireFlag',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='FireSize',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='PixSize',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='Satzen',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='T11',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='T4',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='Temp',
        ),
        migrations.RemoveField(
            model_name='foco',
            name='posicao',
        ),
        migrations.AddField(
            model_name='foco',
            name='arquivo',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foco',
            name='dataregUTC',
            field=models.DateField(default='2015-01-01'),
            preserve_default=False,
        ),
    ]
