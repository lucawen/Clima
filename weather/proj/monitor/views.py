#-*- coding: utf-8 -*-
#!/usr/bin/env python

from django.shortcuts   import render
from monitor.models     import Projeto, Equipe, Alarme, ItemAlarme, FocoFIRMS, FocoWFABBA
from monitor.fma        import FMA
from monitor.dashboard  import DashBoard
from django.template    import RequestContext, loader
from datetime           import datetime
from django.http        import HttpResponse, HttpResponseBadRequest
from django.contrib.gis.geos import Point
from djgeojson.serializers   import Serializer as GeoJSONSerializer
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.gdal.envelope import Envelope 
from monitor.alarme     import FocoToItemAlarme



def focoPopUp(request, chave):
    
    campos = chave.split('X')
    key = int(campos[1])
    registro = None
    if campos[0] == 'F':
       registro = FocoFIRMS.objects.get(pk=key)
    else:
       registro = FocoWFABBA.objects.get(pk=key)

    objRegra = ItemAlarme()
    objRegra = FocoToItemAlarme()
    saida = objRegra.getMixin(registro, objRegra) 

    html = ''
    html += '</ul>'                                    
    html += '<li>ID              :' + str(saida.foco_id) + '</li>'
    html += '<li>Registro        :' + str(saida.dataregUTC) + '</li>'
    html += '<li>Data            :' + str(saida.dataUTC) + '</li>'
    html += '<li>Posicao         :' + u'[{0},{1}]'.format(saida.posicao[0], saida.posicao[1]) + '</li>'
    html += '<li>Temperatura     :' + str(saida.temp) + '</li>'
    html += '<li>Confiabilidade  :' + str(saida.confianca) + '</li>'
    html += '<li>Satellite       :' + saida.satellite+ '</li>'
    html += '<li>Tam.PIxel       :' + str(saida.pixsize) + '</li>'
    html += '<li>Tamanho do Foco :' + str(saida.firesize) + '</li>'
    html += '<li>Alogritmo       :' + str(saida.alg)+ '</li>'
    html += '</ul>'                                    

    return HttpResponse(html,content_type='text/html')




def firmsLayer(request, start, end):

    url = 'http://geonode.terravisiongeo.com.br/geoserver/geonode/ows?service=WFS&version=1.0.0&'
    url +='request=GetFeature&typeName=geonode:_2ferr004_ger_pl_zoneamento_buffer&outputFormat=application/json'

    ds = DataSource(url)
   
    layer = ds[0]
    bounds = Envelope( layer.extent.tuple )

    print bounds

    dataRef1 = datetime.fromtimestamp(int(start)/1000)
    dataRef2 = datetime.fromtimestamp(int(end)/1000)

    query = FocoFIRMS.objects\
        .filter(dataUTC__range= (dataRef1, dataRef2))\
        .filter(posicao__intersects=bounds.wkt) 
    geojson_data = GeoJSONSerializer().serialize( query, use_natural_keys=True)

    return HttpResponse(geojson_data,content_type='text/javascript')

def wfabbaLayer(request, start, end):

    url = 'http://geonode.terravisiongeo.com.br/geoserver/geonode/ows?service=WFS&version=1.0.0&'
    url +='request=GetFeature&typeName=geonode:_2ferr004_ger_pl_zoneamento_buffer&outputFormat=application/json'

    ds = DataSource(url)
   
    layer = ds[0]
    bounds = Envelope( layer.extent.tuple )

    print bounds

    dataRef1 = datetime.fromtimestamp(int(start)/1000)
    dataRef2 = datetime.fromtimestamp(int(end)/1000)

    query = FocoWFABBA.objects\
        .filter(dataUTC__range= (dataRef1, dataRef2))\
        .filter(posicao__intersects=bounds.wkt) 
    geojson_data = GeoJSONSerializer().serialize( query, use_natural_keys=True)

    return HttpResponse(geojson_data,content_type='text/javascript')



    



def dashboard(request, idProjeto):


    data = datetime(2015,10,18)

    start =data.strftime('%d-%m-%Y')
    end = data.strftime('%d-%m-%Y')

    if request.method == "POST":
        start = request.POST.get('txtStart')
        end   = request.POST.get('txtEnd') 

    obj  = DashBoard()
    resultado = obj.execute(idProjeto, data)
    context = RequestContext(request,\
                                {   'result' : resultado, \
                                    'start' : start,\
                                    'end' : end} )

    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context))



def mailalertafoco(request, idAlarme):


    obj = Alarme.objects.get(id = idAlarme)

    objFMA  = FMA()
    objFMA  = objFMA.formula(obj.Projeto_FK.wmo_automatica, obj.data)

    foco = {}
    foco['alarm'] = obj

    foco['focos'] = ItemAlarme.\
                    objects.\
                    filter(Alarme_FK = obj).\
                    order_by('dataUTC')

    foco['para']  = Equipe.objects.filter(Projeto_FK =  obj.Projeto_FK)[0]
    foco['fma']   = objFMA
    foco['caminho']  = 'http://{0}'.format( request.META['HTTP_HOST'] )

    context = RequestContext(request, { 'result' : foco, } )
    template = loader.get_template('mailalertafoco.html')


    return HttpResponse(template.render(context))



