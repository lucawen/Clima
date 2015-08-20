
import  numpy as np

t1 = [ [ 'meses', 'preto',  0.01  ,1.01 ,2.01 ,3.01 ,4.01 ,5.01, 6.01, 7.01, 8.01 ] ,
        [ 'oleo',  'azul' , 10,11,12,13,14,15,16,17,18 ] ,
        [ 'gas',  'verde' ,  910,911,912,913,914,915,916,917,918 ] 
      ]

t2 = np.asarray(t1) 


print np.swapaxes(t2, 0, 1)


