# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_itemalarme_confianca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='focofirms',
            old_name='yyconfidence',
            new_name='confidence',
        ),
    ]
