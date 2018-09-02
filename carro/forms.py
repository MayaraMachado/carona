from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class CarroForm(forms.ModelForm):
    
    class Meta:
        model = Carro
        fields = ['placa', 'cor', 'tipo_idtipo', 'motorista_idmotorista']

    def setMotorista(self, motoristaId):
        data = self.data.copy()
        data['motorista_idmotorista'] = motoristaId
        self.data = data
        return self.data