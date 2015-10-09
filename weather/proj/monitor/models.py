from django.db import models

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


