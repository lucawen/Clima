# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_alarme_projeto_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarme',
            name='figura',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
    ]
