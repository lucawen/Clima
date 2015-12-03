# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0020_auto_20151201_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicao',
            name='dataInc',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
