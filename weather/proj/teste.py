import requests
import base64
import json

class Grafico:

	class Serie:
	    def __init__():
		type = ""
		name = ""
		data = []

	def __init__(self, _titulo, _subtitulo, _unidade, _categorias, _series, _interval, _arquivo):
            self.titulo = _titulo 
            self.subtitulo = _subtitulo 
            self.unidade = _unidade 
            self.categorias = str(_categorias)
            self.series = _series 
            self.interval = _interval 
            self.arquivo = _arquivo 
            self.__getGrafico()


	def __getGrafico(self):
           option = {"infile":self.__getJson(),"constr":"Chart"}
	   url = 'http://tvbhdesenv.terravision.local:3003/'
	   headers = {"Content-Type": "application/json" }
	   r = requests.post(url, headers=headers, data= json.dumps(option)  )
	   imgdata = base64.b64decode(r.content)
	   with open(self.arquivo, 'wb') as f:
	       f.write(imgdata)


	def __getJson(self):
            cfg = "{ title: { text: '" + self.titulo +"' } ,\
                     subtitle: { text: '" + self.subtitulo + "' },\
                     credits : { enabled : true, text : 'powered by: Brandt Meio Ambiente'},\
                     xAxis: { categories: " + self.categorias + " },\
                     yAxis: { min: 0, title: { text: '" + self.unidade + "' }, tickInterval:"  + self.interval + "},\
                     series:" + self.series + " }"
	    return cfg



"""
series = "[\
           { type: 'column', name: 'JAN',  data: [3, 2, 1, 3, 4]        }, \
           { type: 'column', name: 'FEV',  data: [2, 3, 5, 7, 6]        }, \
           { type: 'column', name: 'MAR',  data: [4, 3, 3, 9, 7]        }, \
           { type: 'line',   name: 'VMP',  data: [3, 2.67, 3, 6.33, 3.33] }\
           ]"


graf = Grafico(	'Teste de Titulo',
		'Teste de Subtitulo', 
		'ml', 
		['PT1', 'PT2','PT3','PT4','PT5' ], 
		series, 
		'0.5', 
		'img001.jpeg' )
"""
Grafico('Solidos Totais',\
'Teste de Grafico',\
'mgN/L',\
['RO01', 'RO02', 'RO02A', 'RO03', 'RO05', 'RO06'],\
"[{ type:'column' , name:'Campanha 7/2014',  data:[31.0, 30.0, 32.0, 29.0, 24.0, 15.0]},\
 { type:'line' , name:'VMP',  data:[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}\
]",\
'0.5',\
'ososo.jpeg')





