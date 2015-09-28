from django.contrib.gis.db import models

class Pontos(models.Model):

    upgrh         = models.CharField(max_length=150)
    estacao       = models.CharField(max_length=150)
    descricao	  = models.CharField(max_length=150)
    classeEnquad  = models.CharField(max_length=150)
    datEstab      = models.DateField()	
    datDesatBac	  = models.DateField(null=True, blank=True, default = None)
    Bacia	  = models.CharField(max_length=150)
    SubBacia	  = models.CharField(max_length=150)
    CursoDAgua	  = models.CharField(max_length=150)
    estado	  = models.CharField(max_length=150)
    municipio	  = models.CharField(max_length=150)
    altitude      = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    tipoCorpDAgua = models.CharField(max_length=150)
    posicao       = models.PointField()
    objects       = models.GeoManager()

    @property
    def geom(self):
        return self.posicao

    class Meta:
        ordering = ['descricao',]

    def __unicode__(self):
        return u'{0}'.format(self.descricao)

