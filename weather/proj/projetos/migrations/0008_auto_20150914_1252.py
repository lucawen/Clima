# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0007_auto_20150914_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campanha',
            name='PtoMonit_FK',
        ),
        migrations.AddField(
            model_name='campanha',
            name='Projeto_FK',
            field=models.ForeignKey(default=0, verbose_name=b'Projeto', to='projetos.Projeto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicao',
            name='PtoMonit_FK',
            field=models.ForeignKey(default=0, verbose_name=b'Ponto Monit.', to='projetos.PtoMonit'),
            preserve_default=False,
        ),
    ]
