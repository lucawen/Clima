#-*- coding: utf-8 -*-
#!/usr/bin/env python

from django.shortcuts import render
from django.http import HttpResponse
from monitor.models import Projeto, Equipe, Alarme, ItemAlarme
from monitor.fma    import FMA
from django.template import RequestContext, loader

def mailalertafoco(request, idAlarme):


    obj = Alarme.objects.get(id = idAlarme)

    objFMA  = FMA()
    objFMA  = objFMA.formula(obj.Projeto_FK.wmo_automatica, obj.data)

    print objFMA


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



