# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_auto_20151020_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camada',
            name='coefic',
        ),
        migrations.AddField(
            model_name='camada',
            name='isExtent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='email',
            field=models.EmailField(max_length=120),
        ),
    ]
