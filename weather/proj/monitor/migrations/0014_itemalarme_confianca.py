# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0013_auto_20151022_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemalarme',
            name='confianca',
            field=models.DecimalField(default=0, max_digits=16, decimal_places=4),
        ),
    ]
