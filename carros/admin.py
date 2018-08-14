# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Combustivel, Tipo, tipo_tem_combustivel, Carro
from django.contrib import admin


admin.site.register(Combustivel)
admin.site.register(Tipo)
admin.site.register(tipo_tem_combustivel)
admin.site.register(Carro)