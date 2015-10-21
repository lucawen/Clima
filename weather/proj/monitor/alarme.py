# -*- coding: utf-8 -*- 
#!/usr/bin/env python 

import django
from toolbox.staticmap import StaticMap
from new import  classobj
from monitor.models import Projeto, Camada, Equipe, FocoFIRMS, FocoWFABBA, Alarme
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.geos import GEOSGeometry, Polygon

class AlarmeProc:


    def addAlarme(self, _alg, _id, _msg, pos, idProj):
        query = Alarme.objects.filter(  algoritimo = _alg,\
                                        Projeto_FK_id = idProj,\
                                        foco_id = _id)
        if len(query) == 0:

            #Gera Mapa
            center = [pos[0],pos[1]]

            mapa = StaticMap()
            mapa.markers = [ center, ] 
            path = mapa.processa(center)
            obj = Alarme(algoritimo = _alg,\
                        foco_id       = _id,\
                        figura        = path,\
                        Projeto_FK_id = idProj)
            obj.save()



    def _processaProjeto(self, idProjeto, url):

        ds = DataSource(url)
        layer = ds[0]
        col = layer.get_geoms()
        poly = col[0][0]
        
        for item in FocoFIRMS.objects.all():
            layer.spatial_filter = item.posicao.extent
            if len(layer) > 0:
                self.addAlarme( 'FIRMS',\
                        item.id,\
                        '',\
                        item.posicao,\
                        idProjeto)

        for item in FocoWFABBA.objects.all():
            layer.spatial_filter = item.posicao.extent
            if len(layer) > 0:
                self.addAlarme( 'WFABBA',\
                        item.id,\
                        '',\
                        item.posicao,\
                        idProjeto)
    
    def processa(self):
        for record in Projeto.objects.all():
            objcamada = Camada.objects.filter( Projeto_FK__id = record.id)[0]
            self._processaProjeto(record.id, objcamada[0].url) 



class Alrm:
   
    def confidencialidade_wfabba(self, flag):

        percent = [100,90,85,70,60, 20]

        return percent[flag]


    def __init__(self, _id ): 
          
        record       = self.__getrecordbytable(_id)

        modelo = ('dataregUTC', 'dataUTC', 'posicao', \
                'temp', 'probabilidade', 'satellite',\
                'pixsize', 'firesize' )

        firms  = ('dataregUTC', 'dataUTC', 'posicao', \
                'bright', 'confidence',   'satellite',\
                'scan', 'track')

        wfabba = ('dataregUTC', 'dataUTC', 'posicao',\
                'Temp', 'FireFlag',       'id',  \
                'PixSize', 'FireSize')

        table = firms if type(record) == FocoFIRMS else wfabba

        objInstance = {}
        indice = 0 
        for cpo in table:
            key = modelo[indice]
            value = getattr(record,cpo)
            if key == 'satellite': 
                if table == firms:
                    value = 'Goes-13'
                else:
                    value = 'AQUA' if value == 'A' else 'TERRA' 
            if key == 'probabilidade':
                if table == wfabba:
                    value = self.confidencialidade_wfabba(value)

            objInstance[key]  = value
            indice += 1

        obj = classobj('VAlarme', (object,), objInstance )

        self.record = obj

    def __getrecordbytable(self, _id):

        self.alarme_registro = Alarme.objects.get(id = _id)
        alg = self.alarme_registro.algoritimo
        idModelo = self.alarme_registro.foco_id

        modelo = FocoFIRMS if alg == 'FIRMS' else  FocoWFABBA
        return modelo.objects.get(id = idModelo)

