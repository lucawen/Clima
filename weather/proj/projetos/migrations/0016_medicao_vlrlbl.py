# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0015_auto_20150916_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicao',
            name='vlrLbl',
            field=models.CharField(default=b'', max_length=36, blank=True),
        ),
    ]
