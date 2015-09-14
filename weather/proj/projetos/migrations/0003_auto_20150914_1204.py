# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_remove_ptomonit_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midia',
            name='Projeto_FK',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='Projeto_FK',
        ),
        migrations.RemoveField(
            model_name='texto',
            name='Projeto_FK',
        ),
    ]
