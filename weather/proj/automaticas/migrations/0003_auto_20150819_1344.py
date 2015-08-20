# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automaticas', '0002_auto_20150818_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicaodiaria',
            name='estac',
        ),
        migrations.RemoveField(
            model_name='medicaomensal',
            name='estac',
        ),
        migrations.DeleteModel(
            name='MedicaoDiaria',
        ),
        migrations.DeleteModel(
            name='MedicaoMensal',
        ),
    ]
