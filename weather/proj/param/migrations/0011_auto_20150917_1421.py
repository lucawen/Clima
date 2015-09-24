# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0010_param_texto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidade',
            options={'ordering': ['descricao'], 'verbose_name': 'Unidade', 'verbose_name_plural': 'Unidades'},
        ),
    ]
