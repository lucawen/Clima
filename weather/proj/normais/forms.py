# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django import forms

class PesquisaEstacaoFRM(forms.Form):
    nomeEstacao  = forms.CharField(label='Estação', max_length=100)


