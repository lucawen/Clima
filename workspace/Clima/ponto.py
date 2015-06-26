# -*- coding: utf-8 -*-
#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np


class Serie:
    pass




class Linha:

    
    xLabel = yLabel =title = colunas = None 

    def __init__(self):
        self.series = []    

    def processa(self):
        
        ind =  np.arange(12)
                                
        for item in self.series:
            if item.etiqueta != '':        
                plt.plot(item.valores, item.estilo, color=item.cor,  label=item.etiqueta)
                for i,j in zip(ind,item.valores):            
                    plt.annotate(str(j),xy=(i,j))                            
            if item.preenche:
                plt.fill_between(ind,item.valores,0, color=item.cor, interpolate=True)
                
                
                #val = objserie.valores = [x if x<20 else 20 for x in valores ]                            
                #y2= [ min(x,20)  for x in item.valores]
                #y= [ 0  for x in item.valores]
                #plt.fill_between(ind,val,y, y2, color='red', interpolate=True)              

                                                    
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.title(self.title)
        plt.xticks(ind, self.colunas)
        plt.legend()
        plt.grid(True)        
        plt.show()




valores = [3, 12, 28, 50, 78, 113, 3, 12, 28, 50, 78, 22]



obj = Linha()
obj.title = "Temperaturas "
obj.colunas = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

objserie = Serie()
objserie.valores = valores
objserie.estilo = '-o'
objserie.etiqueta = 'teste0001'
objserie.cor = 'b'
objserie.preenche = False
obj.series.append(objserie)







obj.xLabel = "meses"
obj.yLabel = "mm"
obj.processa()

