from django import forms
from .models import *


class MotoristaForm(forms.ModelForm):
    
    class Meta:
        model = Motorista
        fields = [ 'idmotorista','cnh', 'usuario_idusuario']

    def setUsuario(self, usuarioId):
        data = self.data.copy()
        data['usuario_idusuario'] = usuarioId
        self.data = data
        return self.data