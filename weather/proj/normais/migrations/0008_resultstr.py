# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0007_parametro_planilha'),
    ]

    operations = [
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
                ('Parametro_FK', models.ForeignKey(to='normais.Parametro')),
                ('Station_FK', models.ForeignKey(to='normais.Station')),
            ],
        ),
    ]
