# -*- coding: utf-8 -*-
#!/usr/bin/env python

from projetos import prograph
from datetime import datetime

def run():
    col_pontos = [2376, 2377,2378]
    col_campanha = [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 91, 105, 106, 107, 89, 108, 93, 88, 87, 85, 90, 86, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 109, 110, 92,]
    parametro =  [575, 703, 701, 563, 715, 573, 576, 580, 567, 588, 569, 733, 586, 700, 574, 784, 785, 840, 798, 783, 782, 709, 781, 708, 716, 726,]
    idclasse = 2
    idleg = 0

    print(datetime.now())
    prograph.processa(col_pontos, col_campanha, parametro,  idleg, idclasse)
    print(datetime.now())
    print("Fim")

