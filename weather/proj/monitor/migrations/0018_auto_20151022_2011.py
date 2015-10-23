# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0017_auto_20151022_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarme',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
