# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0003_auto_20150813_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicaoAutomatica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(verbose_name=b'Data')),
                ('temp', models.DecimalField(default=0, verbose_name=b'Temperatura', max_digits=16, decimal_places=2)),
                ('umid', models.DecimalField(default=0, verbose_name=b'Umidade', max_digits=16, decimal_places=2)),
                ('orv', models.DecimalField(default=0, verbose_name=b'Pto.Orvalho', max_digits=16, decimal_places=2)),
                ('press', models.DecimalField(default=0, verbose_name=b'Press\xc3\xa3o', max_digits=16, decimal_places=2)),
                ('vento', models.DecimalField(default=0, verbose_name=b'Vento', max_digits=16, decimal_places=2)),
                ('radiac', models.DecimalField(default=0, verbose_name=b'Radia\xc3\xa7\xc3\xa3o', max_digits=16, decimal_places=2)),
                ('precipt', models.DecimalField(default=0, verbose_name=b'Precipita\xc3\xa7\xc3\xa3o', max_digits=16, decimal_places=2)),
                ('estac', models.ForeignKey(verbose_name=b'Esta\xc3\xa7\xc3\xa3o', to='normais.Station')),
            ],
        ),
    ]
