<<<<<<< HEAD
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Avaliacao, Mensagem
from django.contrib import admin


admin.site.register(Avaliacao)
admin.site.register(Mensagem)
=======
from django.contrib import admin
from .models import Mensagem, Conversa, Avaliacao
# Register your models here.

admin.site.register( Avaliacao)
admin.site.register(Conversa)
admin.site.register( Mensagem)
>>>>>>> 8de7ee5ee40b90b103d254cf169f2f6f70e8a33b
