# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0012_param_intervalo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='param',
            options={'ordering': ['nome'], 'verbose_name': 'Par\xe2metro', 'verbose_name_plural': 'Par\xe2metros'},
        ),
    ]
