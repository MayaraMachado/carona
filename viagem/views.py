from django.shortcuts import render
from .forms import *

def criar_viagem(request):
    breadcrumb1 = 'active'
    form = TrajetoForm(reques.POST or None)
    return render(request, 'pag.html')
