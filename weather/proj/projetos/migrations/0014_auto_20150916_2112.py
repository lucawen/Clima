# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0013_auto_20150916_2039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ptomonit',
            options={},
        ),
        migrations.AddField(
            model_name='ptomonit',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ptomonit',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ptomonit',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ptomonit',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='projetos.PtoMonit', null=True),
        ),
        migrations.AddField(
            model_name='ptomonit',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ptomonit',
            name='tree_id',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
