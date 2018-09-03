from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .functions import *
from usuario_tipo.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Carro

def viagens(request):
    user = request.user
    carros=list(Carro.objects.filter(motorista_idmotorista=user.id))
    #stored procedurepara contar viagens
    return render(request, 'car_list.html', {'carros': carros })

def carro_create(request):
    user = request.user
    motorista =  list(Motorista.objects.filter(usuario_idusuario=user.id))
    if not motorista: 
        print('motorista antes de salvar')
        return render(request, 'car_create.html', {'formulario_titulo':'Motorista' , 'form':MotoristaFormAddCNH(request)})
    else:
        print('motorista depois de salvar')
        return render(request, 'car_create.html', { 'formulario_titulo':'Carro' ,'form':CarroFormMotoristaAdd(request)})