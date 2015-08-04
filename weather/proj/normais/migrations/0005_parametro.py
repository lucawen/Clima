# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0004_auto_20150803_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100)),
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
            ],
        ),
    ]
