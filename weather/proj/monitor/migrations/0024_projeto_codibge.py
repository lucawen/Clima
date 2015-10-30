# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0023_auto_20151028_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='codIBGE',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
    ]
