from django.contrib import admin
from .models import Custo, Viagem, Cidade, Estado, Pais, Trajeto
# Register your models here.


admin.site.register( Custo)
admin.site.register( Viagem)
admin.site.register(Cidade)
admin.site.register( Estado)
admin.site.register( Pais)
admin.site.register( Trajeto)