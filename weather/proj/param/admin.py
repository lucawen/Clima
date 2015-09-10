from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Unidade, Param

# Register your models here.

admin.site.register(Unidade)
admin.site.register(Param, MPTTModelAdmin)

