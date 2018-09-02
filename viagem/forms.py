from django import forms
from .models import *


class TrajetoForm(forms.ModelForm):
    
    class Meta:
        model = Trajeto
        fields = ['idtrajeto','cidade_origem', 'cidade_destino']

