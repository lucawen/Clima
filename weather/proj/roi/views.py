# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.shortcuts import render
from django.template    import RequestContext, loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from roi.models import DeteccaoChoices, CausaacidenteChoices,\
                       ExtratacidenteChoices, AtivagracidenteChoices,\
                       OutrasacidenteChoices,CausadorChoices,\
                       DanosVegetacoChoices, ROI


def roi(request):

    obj = ROI.objects.all()[0]

    print obj.TIPO_AREA_CHOICES[0][0]

    context = RequestContext(request,\
                        { 'form' : obj, \
                          'colDeteccao'      : DeteccaoChoices.objects.all(), \
                          'colCausaAcidente' : CausaacidenteChoices.objects.all(), \
                          'colExtrata'       : ExtratacidenteChoices.objects.all(), \
                          'colAtivAgr'       : AtivagracidenteChoices.objects.all(), \
                          'colOutrasAcidente': OutrasacidenteChoices.objects.all(), \
                          'colCausador'      : CausadorChoices.objects.all(), \
                          'colDanosVegeta'   : DanosVegetacoChoices.objects.all(), \
                          
                        } )
    template = loader.get_template('roi.html')

    return HttpResponse(template.render(context))



