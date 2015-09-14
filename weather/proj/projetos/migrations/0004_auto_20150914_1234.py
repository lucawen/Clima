# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0003_auto_20150914_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midia',
            name='PtoMonit_FK',
        ),
        migrations.RemoveField(
            model_name='texto',
            name='PtoMonit_FK',
        ),
        migrations.AddField(
            model_name='midia',
            name='Medicao_FK',
            field=models.ForeignKey(default=1, verbose_name=b'Medi\xc3\xc3o', to='projetos.Medicao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relatorio',
            name='Projeto_FK',
            field=models.ForeignKey(default=1, verbose_name=b'Projeto', to='projetos.Projeto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='texto',
            name='Medicao_FK',
            field=models.ForeignKey(default=1, verbose_name=b'Medi\xc3\xc3\xa3o', to='projetos.Medicao'),
            preserve_default=False,
        ),
    ]
