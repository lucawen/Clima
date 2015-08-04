# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0006_auto_20150803_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametro',
            name='Planilha',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
