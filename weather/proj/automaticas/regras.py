import psycopg2

class Estacao:
    
    class Registro:
   
        def __init__(self, rec):
            self.codigo = rec[1]
            self.nome   = rec[2]
            self.altitude = rec[3]
            self.ponto    = rec[4]
            self.abertura = rec[5]
            self.omm      = rec[6]


    def __init__(self):
        try:
            connstring = "host='10.3.0.26' dbname='clima' user='postgres' password='wilci5w7'"
            self.db  = psycopg2.connect(connstring)
        except:
             raise


    def getDados(self):
        colec = []
        try:
            cursor = self.db.cursor()
            sql = 'SELECT * FROM "Clima_estacoes" ORDER BY sigla;'
            cursor.execute(sql)
            for record in cursor.fetchall():   
                colec.append(self.Registro(record))
        except:
            raise

        return colec 

    def __del(self):
        self.db.close()







class Medicao:

    class MaxMin:
        def __init__(self, _max, _min, _inst):
            self.vlrmax = _max 
            self.vlrmin = _min
            self.vlrinst = _inst

    class Vent:
        def __init__(self, _vel, _dir, _raj):
            self.vlrvel = _vel
            self.vlrdir = _dir
            self.vlrraj = _raj

    class Registro(Vent, MaxMin):
        def __init__(self, rec):
            self.estac   = rec[2]
            self.data    = rec[3]
            self.hora    = rec[4]
            self.temp    = Medicao.MaxMin(rec[5], rec[6], rec[7])
            self.umidade = Medicao.MaxMin(rec[8], rec[9], rec[10])
            self.orvalho = Medicao.MaxMin(rec[11], rec[12], rec[13])
            self.pressao = Medicao.MaxMin(rec[14], rec[15], rec[16]) 
            self.vento   = Medicao.Vent(rec[17], rec[18], rec[19]) 
            self.radiac  = rec[20]
            self.Precipt = rec[21]


    def __init__(self):
        try:
            connstring = "host='10.3.0.26' dbname='clima' user='postgres' password='wilci5w7'"
            self.db  = psycopg2.connect(connstring)
        except:
            raise
    
    def getDados(self, _chave):
        colec = []
        try:
            cursor = self.db.cursor()
            sql = 'SELECT * FROM "Clima_dadosestacao" WHERE chave LIKE %s ;'
            dados = (_chave, )
            cursor.execute(sql, dados)
            for record in cursor.fetchall():    
                colec.append(self.Registro(record))
        except:
            raise
        
        return colec 

    def __del(self):
        self.db.close()


if __name__ == "__main__":

    res = Medicao().getDados("QTM2NQ%")
    for rec in res:
        print rec.temp.vlrmax, rec.temp.vlrmin, rec.temp.vlrinst

    res = Estacao().getDados()
    for rec in res:
        pass
        print rec.nome, rec.omm

