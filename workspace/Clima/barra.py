# -*- coding: utf-8 -*-
#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt
import Image


class Barra:


    titulo = colunas = linhas = titulosEixos = limites =  arquivo = None
    cor = width = None


    def __autolabel(self, rects):
        # attach some text labels
        for ii,rect in enumerate(rects):
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%s'% (self.linhas[ii]),
                    ha='center', va='bottom')
    


    def processa(self):
        
        N = len(self.colunas)
        ind =  np.arange(N)  # the x locations for the groups
        width = 0.80       # the width of the bars
        
        fig, ax = plt.subplots()
        
        rects1 = ax.bar(ind, self.linhas, self.width, color =self.cor)
        self.__autolabel(rects1)
        
        ax.set_ylabel(self.titulosEixos[0])
        ax.set_xlabel(self.titulosEixos[1])
        ax.set_title(self.titulo)
        ax.set_xticklabels( self.colunas )
        ax.set_xticks(ind+width*.5)
        plt.ylim(self.limites[1])    
        ax.margins(0.05, None)    
        plt.grid(True)
        plt.savefig(self.arquivo)
        plt.show()
    


obj = Barra()
obj.titulo = 'Precipitção Acumulada\nMariana (MG)'
obj.colunas = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")
obj.linhas =(20, 35, 30, 35, 27,20, 35, 30, 35, 27,20, 35)
obj.titulosEixos =('mm', 'meses')
obj.limites = [(0,12),(0,350)]
obj.cor = 'b'
obj.width = 0.80
obj.arquivo = '/home/wilson/teste.jpg'
obj.processa()

