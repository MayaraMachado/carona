from django.contrib import admin
from .models import Carro, Tipo, Combustivel, TipoTemCombustivel
# Register your models here.

admin.site.register(Carro)
admin.site.register(Tipo)
admin.site.register(Combustivel)
admin.site.register(TipoTemCombustivel)
