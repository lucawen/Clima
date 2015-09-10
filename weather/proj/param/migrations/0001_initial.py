# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('monitorado', models.BooleanField(max_length=3, choices=[(0, b'NAO'), (1, b'SIM')])),
                ('vlrTeto', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('vlrPiso', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
                ('tipoParametro', models.CharField(max_length=1, choices=[(0, b'valor'), (1, b'texto'), (2, b'imagem'), (3, b'classe'), (4, b'calculado')])),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='param.Param', null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='param',
            name='unidade_FK',
            field=models.ForeignKey(verbose_name=b'Unidade', to='param.Unidade'),
        ),
    ]
