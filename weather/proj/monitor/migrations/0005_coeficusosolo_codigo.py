# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_coeficusosolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='coeficusosolo',
            name='codigo',
            field=models.IntegerField(default=0),
        ),
    ]
