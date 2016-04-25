# -*- coding: utf-8 -*-
#!/usr/bin/env python

from projetos import prograph
from datetime import datetime

def run():
    col_pontos = [2315, 2316, 2317, 2318]
    col_campanha = [72, 110]
    parametro =  [604, 785, 784, 709, 781, 569, 618, 783, 602, 574, 700, 782, 567, 573, 715, 598, 588, 563, 701, 703, 726]
    idclasse = 2
    idleg = 0

    print(datetime.now())
    prograph.processa(col_pontos, col_campanha, parametro,  idleg, idclasse)
    print(datetime.now())
    print("Fim")

