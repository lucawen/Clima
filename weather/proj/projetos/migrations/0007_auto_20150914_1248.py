# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0006_remove_layer_parametro_fk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('mes', models.IntegerField(default=0)),
                ('ano', models.IntegerField(default=0)),
                ('PtoMonit_FK', models.ForeignKey(verbose_name=b'Ponto Monit.', to='projetos.PtoMonit')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.RemoveField(
            model_name='medicao',
            name='PtoMonit_FK',
        ),
        migrations.AddField(
            model_name='medicao',
            name='Campanha_FK',
            field=models.ForeignKey(default=0, verbose_name=b'Campanha', to='projetos.Campanha'),
            preserve_default=False,
        ),
    ]
