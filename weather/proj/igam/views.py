# -*- coding: utf-8 -*- 
#!/usr/bin/env python

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Pontos


def mapaigam(request):
    context = RequestContext(request)
    template = loader.get_template('mapaIgam.html')   

    return HttpResponse(template.render(context))

def pontoIgam(request, id):

    reg =  Pontos.objects.get(id=id)
    context = RequestContext(request, { 'item': reg } )
    template = loader.get_template('pontoIgam.html')
    return HttpResponse(template.render(context))







