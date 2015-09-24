# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0011_auto_20150917_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='param',
            name='intervalo',
            field=models.DecimalField(default=0, max_digits=16, decimal_places=2),
        ),
    ]
