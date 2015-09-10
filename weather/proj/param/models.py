# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Unidade(models.Model):
    sigla     = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)

    def __unicode__(self):              
        return u'{0}'.format(self.sigla) 


class Param(MPTTModel):
    TipoParam  = ( ('0','valor'),
                   ('1','texto'), 
                   ('2','imagem'), 
                   ('3','classe'), 
                   ('4','calculado'), 
              )

    MONITORADO  = ( ('0','NAO'),
                    ('1','SIM'), 
              )


    nome            = models.CharField(max_length=100, unique=True)
    unidade_FK      = models.ForeignKey(Unidade, verbose_name='Unidade')
    monitorado      = models.CharField(max_length=1, choices=MONITORADO)
    vlrTeto         = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    vlrPiso         = models.DecimalField(default=0, decimal_places=2, max_digits=16)
    tipoParametro   = models.CharField(max_length=1, choices=TipoParam)
    parent          = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    created         = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created']

    class Meta:
        ordering = ['created',]     

    def __unicode__(self):              
        return u'{0}'.format(self.nome) 


