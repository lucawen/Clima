# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0008_auto_20150914_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='url',
            field=models.URLField(max_length=300),
        ),
    ]
