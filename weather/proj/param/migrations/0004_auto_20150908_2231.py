# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0003_auto_20150908_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='monitorado',
            field=models.CharField(max_length=1, choices=[(b'0', b'NAO'), (b'1', b'SIM')]),
        ),
    ]
