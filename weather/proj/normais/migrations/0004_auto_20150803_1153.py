# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0003_auto_20150802_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='Uf',
            new_name='UF',
        ),
    ]
