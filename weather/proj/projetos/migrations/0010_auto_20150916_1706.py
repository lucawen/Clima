# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0009_auto_20150916_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campanha',
            options={'ordering': ['nome'], 'verbose_name': 'Campanha', 'verbose_name_plural': 'Campanhas'},
        ),
        migrations.AlterModelOptions(
            name='layer',
            options={'ordering': ['nome'], 'verbose_name': 'Camada', 'verbose_name_plural': 'Camadas'},
        ),
        migrations.AlterModelOptions(
            name='medicao',
            options={'ordering': ['data'], 'verbose_name': 'Medicao', 'verbose_name_plural': 'Medi\xe7\xf5es'},
        ),
        migrations.AlterModelOptions(
            name='midia',
            options={'ordering': ['nome'], 'verbose_name': 'Midia', 'verbose_name_plural': 'Midia'},
        ),
        migrations.AlterModelOptions(
            name='projeto',
            options={'ordering': ['nome'], 'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
        migrations.AlterModelOptions(
            name='ptomonit',
            options={'ordering': ['nome'], 'verbose_name': 'Ponto de Monitoramento', 'verbose_name_plural': 'Pontos de Monitoramento'},
        ),
        migrations.RemoveField(
            model_name='layer',
            name='url',
        ),
        migrations.AddField(
            model_name='medicao',
            name='controle',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campanha',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=b'Campanha'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=b'Layer'),
        ),
        migrations.AlterField(
            model_name='medicao',
            name='dataInc',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=b'Projeto'),
        ),
        migrations.AlterField(
            model_name='ptomonit',
            name='nome',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Pto.Monit.'),
        ),
    ]
