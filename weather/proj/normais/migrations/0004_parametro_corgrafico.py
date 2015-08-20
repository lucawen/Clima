# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import paintstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('normais', '0003_auto_20150813_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametro',
            name='corGrafico',
            field=paintstore.fields.ColorPickerField(default='#000000', help_text=b'Clique no campo para abrir o colorpicker.', max_length=7),
            preserve_default=False,
        ),
    ]
