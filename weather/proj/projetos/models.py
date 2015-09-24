# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.db import models
from paintstore.fields import ColorPickerField
from param.models import Param
from mptt.models import MPTTModel, TreeForeignKey
from datetime import datetime


# Create your models. here.

class Projeto(models.Model):

    codigo = models.CharField(max_length=6)
    nome = models.CharField(max_length=100, verbose_name='Projeto')
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
	ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


class Layer(models.Model):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    nome        = models.CharField(max_length=100, verbose_name='Layer')
    url         = models.URLField(max_length=300, verbose_name='URL Layer'),
    
    class Meta:
        verbose_name = 'Camada'
        verbose_name_plural = 'Camadas'
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 



class PtoMonit(MPTTModel):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    Layer_FK    = models.ForeignKey(Layer, verbose_name="Layer" )
    sigla       = models.CharField(max_length=15, default='', verbose_name='Codigo do Ponto.', unique=True, db_index=True)
    nome        = models.CharField(max_length=2200, default='', verbose_name='Pto.Monit.')
    ObjectID    = models.IntegerField(default=0)
    parent      = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    created     = models.DateTimeField(auto_now_add=True)
    
    class MPTTMeta:
        order_insertion_by = ['sigla']
        verbose_name = 'Ponto de Monitoramento'
        verbose_name_plural = 'Pontos de Monitoramento'
        ordering = ['sigla',]     

    def __unicode__(self):              
        return u'{0}-{1}'.format(self.sigla, self.nome) 

class Campanha(models.Model):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    nome        = models.CharField(max_length=100,  verbose_name='Campanha')
    mes         = models.IntegerField(default=0)
    ano         = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


class Medicao(models.Model):

    Campanha_FK = models.ForeignKey(Campanha, verbose_name="Campanha" )
    PtoMonit_FK  = models.ForeignKey(PtoMonit, verbose_name="Ponto Monit." )
    Parametro_FK= models.ForeignKey(Param, verbose_name="Parametro" )
    controle    = models.CharField(max_length=20, blank=True)
    data        = models.DateField()
    dataInc     = models.DateField(default=datetime.now, blank=True)
    vlr         = models.DecimalField(default=0, decimal_places=2, max_digits=16)    
    vlrLbl      = models.CharField(default='',  max_length=36, blank=True)    
 
    class Meta:
        verbose_name = u'Medicao'
        verbose_name_plural = u'Medições'
        ordering = ['data',]     

    def __unicode__(self):              
        return u'{0}'.format(self.controle) 


class Midia(models.Model):

    Medicao_FK  = models.ForeignKey(Medicao, verbose_name="Medicao" )
    nome        = models.CharField(max_length=100, default='')
    url         = models.CharField(max_length=300)
    data        = models.DateField()
    docfile     = models.FileField(max_length=300,null=True, upload_to='midia')

    class Meta:
        verbose_name = u'Midia'
        verbose_name_plural = u'Midia'
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


class Texto(models.Model):

    Medicao_FK  = models.ForeignKey(Medicao, verbose_name="Medicao" )
    descricao   = models.TextField(default='')
    data        = models.DateField()

    class Meta:
        ordering = ['descricao',]     

    def __unicode__(self):              
        return u'{0}'.format(self.descricao) 


class Relatorio(models.Model):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    Parametro_FK= models.ForeignKey(Param, verbose_name="Parametro" )
    descricao   = models.TextField(default='')
    data        = models.DateField()
    class Meta:
        ordering = ['descricao',]     

    def __unicode__(self):              
        return u'{0}'.format(self.descricao) 


