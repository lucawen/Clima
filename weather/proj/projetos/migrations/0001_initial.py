# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('param', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=300)),
                ('Parametro_FK', models.ForeignKey(verbose_name=b'Parametro', to='param.Param')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Medicao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('dataInc', models.DateField()),
                ('vlr', models.DecimalField(default=0, max_digits=16, decimal_places=2)),
            ],
            options={
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('url', models.CharField(max_length=300)),
                ('data', models.DateField()),
                ('docfile', models.FileField(max_length=300, null=True, upload_to=b'midia')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=6)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='PtoMonit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('url', models.CharField(max_length=300)),
                ('ObjectID', models.IntegerField(default=0)),
                ('Layer_FK', models.ForeignKey(verbose_name=b'Layer', to='projetos.Layer')),
                ('Parametro_FK', models.ForeignKey(verbose_name=b'Parametro', to='param.Param')),
                ('Projeto_FK', models.ForeignKey(verbose_name=b'Projeto', to='projetos.Projeto')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField(default=b'')),
                ('data', models.DateField()),
                ('Parametro_FK', models.ForeignKey(verbose_name=b'Parametro', to='param.Param')),
                ('Projeto_FK', models.ForeignKey(verbose_name=b'Projeto', to='projetos.Projeto')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField(default=b'')),
                ('data', models.DateField()),
                ('Projeto_FK', models.ForeignKey(verbose_name=b'Projeto', to='projetos.Projeto')),
                ('PtoMonit_FK', models.ForeignKey(verbose_name=b'Ponto Monit.', to='projetos.PtoMonit')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.AddField(
            model_name='midia',
            name='Projeto_FK',
            field=models.ForeignKey(verbose_name=b'Projeto', to='projetos.Projeto'),
        ),
        migrations.AddField(
            model_name='midia',
            name='PtoMonit_FK',
            field=models.ForeignKey(verbose_name=b'Ponto Monit.', to='projetos.PtoMonit'),
        ),
        migrations.AddField(
            model_name='medicao',
            name='PtoMonit_FK',
            field=models.ForeignKey(verbose_name=b'Ponto Monit.', to='projetos.PtoMonit'),
        ),
        migrations.AddField(
            model_name='layer',
            name='Projeto_FK',
            field=models.ForeignKey(verbose_name=b'Projeto', to='projetos.Projeto'),
        ),
    ]
