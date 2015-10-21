# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0010_auto_20151020_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarme',
            name='Projeto_FK',
            field=models.ForeignKey(default=1, verbose_name=b'Projeto', to='monitor.Projeto'),
            preserve_default=False,
        ),
    ]
