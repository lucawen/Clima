# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0006_param_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='param',
            options={'ordering': ['created']},
        ),
    ]
