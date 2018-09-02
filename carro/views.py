from django.shortcuts import render
from .functions import *


def carro_create(request):
    context ={
        'form': CarroFormMotoristaAdd(request)
    }
    return render(request, 'car_create.html', context)