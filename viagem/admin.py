# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Pais, Estado, Cidade, Viagem, Trajeto
from django.contrib import admin

admin.site.register( Pais)
admin.site.register( Estado)
admin.site.register( Cidade)
admin.site.register( Viagem)
admin.site.register( Trajeto)