# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0014_auto_20150916_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptomonit',
            name='nome',
            field=models.CharField(default=b'', max_length=2200, verbose_name=b'Pto.Monit.'),
        ),
    ]