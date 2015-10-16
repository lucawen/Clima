from django.contrib import admin
from monitor.models import Projeto, Camada, Equipe


# Register your models here.
class EquipeDetailInline(admin.TabularInline):        
    model = Equipe
    fields = ['nome','email', 'foneFixo', 'foneCel', ]    
    show_change_link = True           
    extra = 0

class CamadaDetailInline(admin.TabularInline):        
    model = Camada
    fields = ['nome','url', 'coefic', ]    
    show_change_link = True           
    extra = 0


class ProjetoAdmin(admin.ModelAdmin):
	list_filter = ('codigo', 'nome', 'wmo_normais', 'wmo_automatica',)

	list_display = ('codigo', 'nome', 'wmo_normais', 'wmo_automatica',)
	
	inlines = [EquipeDetailInline, CamadaDetailInline, ]




admin.site.register(Projeto, ProjetoAdmin)


