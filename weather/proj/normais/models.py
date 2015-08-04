# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.db import models

# Create your models. here.

class Station(models.Model):
    Codigo = models.CharField(max_length=6)
    Nome = models.CharField(max_length=100)
    Estado = models.CharField(max_length=50)
    UF = models.CharField(max_length=2)
    Altitude = models.DecimalField(default=0, decimal_places=2, max_digits=16) 
    Tmed = models.CharField(max_length=1)
    Tmax = models.CharField(max_length=1)
    Tmin = models.CharField(max_length=1)
    TmaxAbs = models.CharField(max_length=1)
    TminAbs = models.CharField(max_length=1)
    Pres = models.CharField(max_length=1)
    Inso = models.CharField(max_length=1)
    Evap = models.CharField(max_length=1)
    Neb = models.CharField(max_length=1)
    NebHora = models.CharField(max_length=1)
    UR = models.CharField(max_length=1)
    URHora = models.CharField(max_length=1)
    Prec = models.CharField(max_length=1)
    PrecMax = models.CharField(max_length=1)
    PrecNDias = models.CharField(max_length=1)
    PDec = models.CharField(max_length=1)
    PdecND = models.CharField(max_length=1)
    NPSec = models.CharField(max_length=2)
    VentoInt = models.CharField(max_length=1)
    Ventou = models.CharField(max_length=1)
    Ventov = models.CharField(max_length=1)
    VentoDirRes = models.CharField(max_length=1)
    VentoDirPred = models.CharField(max_length=1)
    NNormais  = models.IntegerField(default=0)
    LatLong = models.CharField(max_length=100)
     
    def __unicode__(self):              
        return u'{0}'.format(self.Codigo) 

class Classe(models.Model):
    Nome = models.CharField(max_length=100)

    def __unicode__(self):              
        return u'{0}'.format(self.Nome) 

class Parametro(models.Model):
    Nome = models.CharField(max_length=100)
    Classe_FK = models.ForeignKey(Classe, null=True, blank=True, default = None)
    Planilha = models.CharField(max_length=200, default='')
    jan = models.IntegerField(default=0)
    fev = models.IntegerField(default=0)
    mar = models.IntegerField(default=0)
    abr = models.IntegerField(default=0)
    mai = models.IntegerField(default=0)
    jun = models.IntegerField(default=0)
    jul = models.IntegerField(default=0)
    ago = models.IntegerField(default=0)
    stb = models.IntegerField(default=0)
    out = models.IntegerField(default=0)
    nov = models.IntegerField(default=0)
    dez = models.IntegerField(default=0)
    tot = models.IntegerField(default=0)

    def __unicode__(self):              
        return u'{0}'.format(self.Nome) 

class ResultStr(models.Model):

    Station_FK  = models.ForeignKey(Station)
    Parametro_FK  = models.ForeignKey(Parametro)
    jan = models.CharField(max_length=20, default='')
    fev = models.CharField(max_length=20, default='')
    mar = models.CharField(max_length=20, default='')
    abr = models.CharField(max_length=20, default='')
    mai = models.CharField(max_length=20, default='')
    jun = models.CharField(max_length=20, default='')
    jul = models.CharField(max_length=20, default='')
    ago = models.CharField(max_length=20, default='')
    stb = models.CharField(max_length=20, default='')
    out = models.CharField(max_length=20, default='')
    nov = models.CharField(max_length=20, default='')
    dez = models.CharField(max_length=20, default='')
    tot = models.CharField(max_length=20, default='')


    def __unicode__(self):              
        return u'{0}'.format(self.Parametro_FK) 

class Resultado(models.Model):

    Station_FK  = models.ForeignKey(Station)
    Parametro_FK  = models.ForeignKey(Parametro)
    jan = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    fev = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    mar = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    abr = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    mai = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    jun = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    jul = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    ago = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    stb = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    out = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    nov = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    dez = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    tot = models.DecimalField(default=0, decimal_places=2, max_digits=16)


    def __unicode__(self):              
        return u'{0}'.format(self.Parametro_FK) 



