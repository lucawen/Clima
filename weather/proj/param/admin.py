from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Unidade, Param
from django_mptt_admin.admin import DjangoMpttAdmin

# Register your models here.

class ParamAdmin(DjangoMpttAdmin):
	pass


admin.site.register(Unidade)
admin.site.register(Param, ParamAdmin)

