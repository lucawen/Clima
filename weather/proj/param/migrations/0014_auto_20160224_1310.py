# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 16:10
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0013_auto_20150924_1752'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='param',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]