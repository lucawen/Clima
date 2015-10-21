#-*- coding: utf-8 -*-
#!/usr/bin/env python

from django.shortcuts import render
from django.http import HttpResponse
from monitor.models import Projeto, Equipe
from monitor.fma    import FMA
from monitor.alarme import Alrm
from django.template import RequestContext, loader

def mailalertafoco(request, idAlarme):

    obj = Alrm(idAlarme)
    projRecord =   Projeto.objects.\
                                get(id = obj.alarme_registro.Projeto_FK_id)

    objFMA = FMA()
    colecao = objFMA.formula(projRecord.wmo_automatica)

    foco = {}
    foco['foco']  = obj.record
    foco['alarm'] = obj.alarme_registro
    foco['para']  = Equipe.objects.\
                           filter(Projeto_FK_id = projRecord.id)[0]
    foco['fma']   = objFMA.formula(projRecord.wmo_automatica)
    foco['proj']  = projRecord
    foco['caminho']  = 'http://{0}'.format( request.META['HTTP_HOST'] )

    context = RequestContext(request, { 'result' : foco, } )
    template = loader.get_template('mailalertafoco.html')

    return HttpResponse(template.render(context))



