from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Projeto(models.Model):

    codigo = models.CharField(max_length=6)
    nome = models.CharField(max_length=100, verbose_name='Projeto')
    wmo_normais = models.CharField(max_length=6)
    wmo_automatica = models.CharField(max_length=6)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
	ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


class Camada(models.Model):

    Projeto_FK  = models.ForeignKey(Projeto, verbose_name="Projeto" )
    nome        = models.CharField(max_length=100, verbose_name='Layer')
    url         = models.URLField(max_length=300, verbose_name='URL Layer')
    
    class Meta:
        verbose_name = 'Camada'
        verbose_name_plural = 'Camadas'
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


class Equipe(models.Model):

    Projeto_FK    = models.ForeignKey(Projeto, verbose_name="Projeto" )
    nome          = models.CharField(max_length=100)
    email         = models.URLField(max_length=120)
    foneFixo      = models.CharField(max_length=20 )
    foneCel       = models.CharField(max_length=20)

    
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 

class FocoWFABBA(models.Model):
    dataUTC     = models.DateTimeField()
    dataregUTC  = models.DateTimeField()
    arquivo     = models.CharField(max_length=100)
    posicao     = models.PointField()
    Satzen      = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    PixSize     = models.DecimalField(default=0, decimal_places=4, max_digits=16)
    T4          = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    T11         = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    FireSize    = models.DecimalField(default=0, decimal_places=4, max_digits=16)
    Temp        = models.IntegerField(default=0)
    FRP         = models.IntegerField(default=0)
    Ecosystem   = models.IntegerField(default=0)
    FireFlag    = models.IntegerField(default=0)
    objects = models.GeoManager()

    @property
    def geom(self):
        return self.posicao

    class Meta:
        ordering = ['dataUTC',]     

    def __unicode__(self):              
        return u'{0}'.format(self.dataUTC) 

class FocoFIRMS(models.Model):
    #https://earthdata.nasa.gov/files/README_TXT.pdf

    dataregUTC = models.DateTimeField()
    posicao    = models.PointField()
    bright     = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    scan       = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    track      = models.DecimalField(default=0, decimal_places=4, max_digits=16)
    dataUTC    = models.DateTimeField()
    satellite  = models.CharField(max_length=1)
    confidence = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    version    = models.CharField(max_length=5)
    brightT31  = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    frp        = models.DecimalField(default=0, decimal_places=4, max_digits=16)
    objects = models.GeoManager()

    @property
    def geom(self):
        return self.posicao

    class Meta:
        ordering = ['dataUTC',]     

    def __unicode__(self):              
        return u'{0}'.format(self.dataUTC) 


