# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='email',
            field=models.URLField(max_length=120),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='foneCel',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='foneFixo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
