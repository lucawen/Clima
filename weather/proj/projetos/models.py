# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.db import models
from paintstore.fields import ColorPickerField
from param.models import Param
# Create your models. here.

class Projeto(models.Model):

    codigo = models.CharField(max_length=6)
    nome = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


class Layer(models.Model):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    nome        = models.CharField(max_length=100)
    url         = models.CharField(max_length=300)
    
    class Meta:
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 



class PtoMonit(models.Model):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    Parametro_FK= models.ForeignKey(Param, verbose_name="Parametro" )
    Layer_FK    = models.ForeignKey(Layer, verbose_name="Layer" )
    nome        = models.CharField(max_length=100, default='')
    ObjectID    = models.IntegerField(default=0)

    class Meta:
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 

class Campanha(models.Model):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    nome        = models.CharField(max_length=100)
    mes         = models.IntegerField(default=0)
    ano         = models.IntegerField(default=0)

    class Meta:
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


class Medicao(models.Model):

    Campanha_FK = models.ForeignKey(Campanha, verbose_name="Campanha" )
    PtoMonit_FK  = models.ForeignKey(PtoMonit, verbose_name="Ponto Monit." )
    data        = models.DateField()
    dataInc     = models.DateField()
    vlr         = models.DecimalField(default=0, decimal_places=2, max_digits=16)    
 
    class Meta:
        ordering = ['data',]     

    def __unicode__(self):              
        return u'{0}'.format(self.data) 


class Midia(models.Model):

    Medicao_FK  = models.ForeignKey(Medicao, verbose_name="Medicao" )
    nome        = models.CharField(max_length=100, default='')
    url         = models.CharField(max_length=300)
    data        = models.DateField()
    docfile     = models.FileField(max_length=300,null=True, upload_to='midia')

    class Meta:
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


