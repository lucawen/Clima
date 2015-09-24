# -*- coding: utf-8 -*- 
#!/usr/bin/env python 


from django.db import models
from projetos.models import Campanha, PtoMonit
from param.models import Param
from django import forms


class frmGrafico(forms.Form):
    parametro = forms.ModelChoiceField(queryset=Param.objects.all())
    pontos    = forms.ModelChoiceField(queryset=PtoMonit.objects.filter(level=1).all())
    campanhas = forms.ModelMultipleChoiceField(queryset=Campanha.objects.all())


