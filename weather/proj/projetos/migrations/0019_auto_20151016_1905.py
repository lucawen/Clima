# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0018_auto_20150924_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicao',
            options={'ordering': ['data'], 'verbose_name': 'Medicao', 'verbose_name_plural': 'Medicoes'},
        ),
    ]
