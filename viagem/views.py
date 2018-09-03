from django.shortcuts import render
from .forms import *
from django.db import connection
from  .models import *


def criar_viagem(request):
    form = TrajetoForm(reques.POST or None)
    return render(request, 'pag.html')

def listar_viagem(request):
    viagens = Viagem.objects.all()
    context={
        'viagens' : viagens,
    }
    return render(request, 'todas_viagens_list.html', context)

def listar_mensagens(request, id):
    sql_string = "select v.idviagem, m.mensagem, m.usuario_idusuario, a.first_name, m.data_hora from viagem v join conversa c on v.idviagem = c.viagem_idviagem join mensagem m on c.idconversa = m.conversa_idconversa join auth_user a on m.usuario_idusuario = a.id where v.idviagem = "+ str(id)
    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        row = cursor.fetchall()
    context={
        'mensagens' : row,
    }
    return render(request, 'mensagem.html', context)


