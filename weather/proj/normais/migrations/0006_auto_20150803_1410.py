# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0005_parametro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jan', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('fev', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('mar', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('abr', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('mai', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('jun', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('jul', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('ago', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('stb', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('out', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('nov', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('dez', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('tot', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('Parametro_FK', models.ForeignKey(to='normais.Parametro')),
                ('Station_FK', models.ForeignKey(to='normais.Station')),
            ],
        ),
        migrations.AddField(
            model_name='parametro',
            name='Classe_FK',
            field=models.ForeignKey(default=None, blank=True, to='normais.Classe', null=True),
        ),
    ]
