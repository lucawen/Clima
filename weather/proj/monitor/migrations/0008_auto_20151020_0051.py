# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_alarme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarme',
            name='msg',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
