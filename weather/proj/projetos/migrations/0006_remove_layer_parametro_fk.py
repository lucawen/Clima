# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0005_auto_20150914_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='Parametro_FK',
        ),
    ]
