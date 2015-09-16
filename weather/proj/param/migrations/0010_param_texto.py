# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0009_auto_20150916_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='param',
            name='texto',
            field=models.TextField(null=True, blank=True),
        ),
    ]
