from pacote.tools import Tools
from os import remove
import psycopg2

class Estacao:        
    def _init__(self):
        self.codEstacao = ""

    def getEstacoes(self, db):    
        cursor = db.cursor()
        colEstacoes = []
        cursor.execute('SELECT codigo FROM "Clima_estacoes";')
        registros = cursor.fetchall()
        for item in registros:
            #print "col.append('{0}')".format(item[0])
            colEstacoes.append(item[0])            
        return colEstacoes

class DadosEstacao:

    def __init__(self):            
        self.chave = self.codEstac = self.Data = self.Hora = None  
        self.TempInst = None
        self.TempMax = self.TempMin = self.UmidInst = self.UmidMax = None 
        self.UmidMin = self.PtoOrvInst = self.PtoOrvMax = self.PtoOrvMin = None 
        self.PressInst = self.PressMax = self.PressMin = self.VentVel = None 
        self.VentDir = self.VentRaj = self.Radiacao = self.Chuva = None
        
    def FromLinha(self, _tabela, estacao):                
   
        chave = estacao + _tabela[0] + _tabela[1]
        dt = Tools.tryMDY(_tabela[0])
        
        self.chave = chave
        self.codEstac = estacao
        self.Data = dt
        self.Hora = int(_tabela[1])      
        self.TempInst = Tools.tryFloat(_tabela[2])
        self.TempMax = Tools.tryFloat(_tabela[3])
        self.TempMin = Tools.tryFloat(_tabela[4])
        self.UmidInst = Tools.tryFloat(_tabela[5])
        self.UmidMax = Tools.tryFloat(_tabela[6])
        self.UmidMin = Tools.tryFloat(_tabela[7])
        self.PtoOrvInst = Tools.tryFloat(_tabela[8])
        self.PtoOrvMax = Tools.tryFloat(_tabela[9])
        self.PtoOrvMin = Tools.tryFloat(_tabela[10])
        self.PressInst = Tools.tryFloat(_tabela[11])
        self.PressMax = Tools.tryFloat(_tabela[12])
        self.PressMin = Tools.tryFloat(_tabela[13])
        self.VentVel = Tools.tryFloat(_tabela[14])
        self.VentDir = Tools.tryFloat(_tabela[15][:-1])
        self.VentRaj = Tools.tryFloat(_tabela[16])
        self.Radiacao = Tools.tryFloat(_tabela[17])
        self.Chuva = Tools.tryFloat(_tabela[18])      
        
       
    def getResult(self, db):
        sql = 'SELECT "Data", count(*) FROM "Clima_dadosestacao" GROUP BY "Data" ORDER BY "Data" DESC LIMIT 20;'
        cursor = db.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()

        return registros



    def __gravaRegistros(self, db, dados):    
        cursor = db.cursor()        
        for ln in dados:                            
            try:   
                cursor = db.cursor()        
                try:              
                    sql = 'INSERT INTO "Clima_dadosestacao"(chave, "codEstac", "Data", "Hora", "TempInst", "TempMax","TempMin", "UmidInst", "UmidMax", "UmidMin", "PtoOrvInst", "PtoOrvMax","PtoOrvMin", "PressInst", "PressMax", "PressMin", "VentVel","VentDir", "VentRaj", "Radiacao", "Chuva", estacao_id) VALUES( %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s);'
                    dados = ( ln['chave'], ln['codEstac'], ln['Data'], ln['Hora'],ln['TempInst'],ln['TempMax'],ln['TempMin'],ln['UmidInst'],ln['UmidMax'],ln['UmidMin'],ln['PtoOrvInst'],ln['PtoOrvMax'],ln['PtoOrvMin'],ln['PressInst'],ln['PressMax'],ln['PressMin'],ln['VentVel'],ln['VentDir'],ln['VentRaj'],ln['Radiacao'],ln['Chuva'],1,  )
                    cursor.execute(sql, dados)            
                    db.commit()
                except psycopg2.IntegrityError:
                    db.rollback()
                else:
                    db.commit()    
            except:
                raise
    
    def InsereDB(self, db, path):            
        for arquivo in Tools.LerArquivosDiretorio(path, '.json'):
            arquivo = path + arquivo
            conteudo = Tools.ExtraiStringArquivo(arquivo)                                    
            self.__gravaRegistros(db, conteudo)
            print arquivo
            remove(arquivo)
