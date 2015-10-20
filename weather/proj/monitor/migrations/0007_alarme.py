# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20151016_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isenviado', models.IntegerField(default=0)),
                ('algoritimo', models.CharField(max_length=1)),
                ('foco_id', models.IntegerField(default=0)),
                ('msg', models.TextField(max_length=1)),
            ],
        ),
    ]
