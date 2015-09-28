# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontos',
            name='datDesatBac',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
