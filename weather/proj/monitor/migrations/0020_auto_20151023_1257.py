# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0019_auto_20151023_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemalarme',
            old_name='fireSize',
            new_name='firesize',
        ),
    ]
