import django
import normais.models as db

def run():
    col = db.Parametro.objects.all().order_by('codigo')
    for item in col:
        print item.codigo, item.Nome, item.codigo


