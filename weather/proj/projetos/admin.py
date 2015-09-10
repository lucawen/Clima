from django.contrib import admin
from .models import Projeto, Layer
from .models import PtoMonit, Medicao
from .models import Midia, Texto
from .models import Relatorio
                    
admin.site.register(Projeto)
admin.site.register(Layer)
admin.site.register(PtoMonit)
admin.site.register(Medicao)
admin.site.register(Midia)
admin.site.register(Texto)
admin.site.register(Relatorio)



# Register your models here.
