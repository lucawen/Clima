# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_auto_20151020_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarme',
            name='algoritimo',
            field=models.CharField(max_length=6),
        ),
    ]
