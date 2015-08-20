# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='posicao',
            field=django.contrib.gis.db.models.fields.PointField(default='SRID=4326;POINT(0.0 0.0)', srid=4326),
            preserve_default=False,
        ),
    ]
