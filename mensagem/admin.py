from django.contrib import admin
from .models import Mensagem, Conversa, Avaliacao
# Register your models here.

admin.site.register( Avaliacao)
admin.site.register(Conversa)
admin.site.register( Mensagem)