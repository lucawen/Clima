# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0002_auto_20150802_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='Colunas4',
        ),
        migrations.RemoveField(
            model_name='station',
            name='Colunas5',
        ),
    ]
