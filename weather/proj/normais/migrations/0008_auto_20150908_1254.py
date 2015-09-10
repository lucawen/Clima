# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0007_auto_20150908_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focoitem',
            name='foco_FK',
            field=models.ForeignKey(verbose_name=b'Foco', to='normais.Foco'),
        ),
    ]
