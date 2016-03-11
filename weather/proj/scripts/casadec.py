# -*- coding: utf-8 -*-
#!/usr/bin/env python

import pandas as pd
from param.models import Param

def run():
    df = pd.read_excel('/media/projeto_cemig/01_PROJETO SOFTWARE/Casas_decimais.xlsx', 0, index_col=0)

    for item in df.index:
        try:
            reg = Param.objects.get(pk=item)
        except:
            continue
        it = df.loc[item]
        if reg.nome.replace(' ','') == 'nan':
            reg.texto = ''
            Param.save(reg)
        if it.Texto != 'nan':
            reg.texto = it.Texto
            Param.save(reg)

