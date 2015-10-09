# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Layer')),
                ('url', models.URLField(max_length=300, verbose_name=b'URL Layer')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Camada',
                'verbose_name_plural': 'Camadas',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Layer')),
                ('email', models.URLField(max_length=300, verbose_name=b'URL Layer')),
                ('foneFixo', models.URLField(max_length=300)),
                ('foneCel', models.CharField(max_length=13)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=6)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Projeto')),
                ('wmo_normais', models.CharField(max_length=6)),
                ('wmo_automatica', models.CharField(max_length=6)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.AddField(
            model_name='equipe',
            name='Projeto_FK',
            field=models.ForeignKey(verbose_name=b'Projeto', to='monitor.Projeto'),
        ),
        migrations.AddField(
            model_name='camada',
            name='Projeto_FK',
            field=models.ForeignKey(verbose_name=b'Projeto', to='monitor.Projeto'),
        ),
    ]
