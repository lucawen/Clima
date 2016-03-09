# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Unidade(models.Model):

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['descricao',]

    sigla     = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return u'{0}'.format(self.sigla)


class Param(MPTTModel):

    class Meta:
        verbose_name = u'Parâmetro'
        verbose_name_plural = u'Parâmetros'
        ordering = ['nome',]

    TipoParam  = ( ('0','valor'),
                   ('1','texto'),
                   ('2','imagem'),
                   ('3','classe'),
                   ('4','calculado'),
              )

    MONITORADO  = ( ('0','NAO'),
                    ('1','SIM'),
              )


    nome            = models.CharField(max_length=300, unique=True, verbose_name='Parametro')
    unidade_FK      = models.ForeignKey(Unidade, verbose_name='Unidade')
    monitorado      = models.CharField(max_length=1, choices=MONITORADO)
    vlrTeto         = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    vlrPiso         = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    decimais        = models.IntegerField(default=0)
    intervalo       = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    tipoParametro   = models.CharField(max_length=1, choices=TipoParam)
    parent          = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    created         = models.DateTimeField(auto_now_add=True)
    texto           = models.TextField(null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['nome']

    def __unicode__(self):
        return u'{0}'.format(self.nome)


class Legislacao(models.Model):

    class Meta:
        verbose_name = u'Legislação'
        verbose_name_plural = u'Legislação'

    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return u'{0}'.format(self.descricao)

class Classe(models.Model):

    class Meta:
        verbose_name = u'Classe VMP'
        verbose_name_plural = u'Classe VMP'

    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return u'{0}'.format(self.descricao)

class Limites(models.Model):
    class Meta:
        verbose_name = u'Limites'
        verbose_name_plural = u'Limites'

    parametro_FK  = models.ForeignKey(Param, verbose_name='Parametro')
    legislacao_FK = models.ForeignKey(Legislacao, verbose_name=u'Legislacão')
    classe_FK  = models.ForeignKey(Classe, verbose_name=u'Classe')
    vlr_max  = models.DecimalField(default=0, decimal_places=4, max_digits=16)
    vlr_min  = models.DecimalField(default=0, decimal_places=4, max_digits=16)


