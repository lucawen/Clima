# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0010_auto_20150916_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicao',
            name='controle',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
