from django.shortcuts import render
from .forms import *
from viagem.models import Cidade
from django.db import connection



# Create your views here.
def index(request):
    context = {
        'titulo_variavel': 'CaronaApp'
    }
    return render(request,'index.html', context)

def query(request):
    form = QueryForm(request.POST or None)
    if form.is_valid():
        sql_string = form.cleaned_data['query']
        with connection.cursor() as cursor:
            cursor.execute(sql_string)
            row = cursor.fetchall()
            print(row)
        return render(request, 'query_list.html', {'row':row, 'query': sql_string})

    context = {
        'form' : form
    }
    return render(request, 'query.html', context)

def query_sql(request, sql):
    with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchall()
            print(row)
    return render(request, 'query_list.html', {'row':row, 'query': sql})




def query_cidade(request):
    form = QueryForm(request.POST or None)
    cidade_busca = None
    if form.is_valid():
        cidade_busca = Cidade.buscador_cidade(form.cleaned_data['query'])
        print(cidade_busca)
    
    context = {
        'titulo_variavel': 'CaronaApp',
        'form' : form,
        'cidades' : cidade_busca
    }
    return render(request,'viagem_list.html', context) 

def top_motorista(request):
    sql_string="select * from (select a.id, a.first_name, a.last_name, avg(av.nota) as media, (select count (1) from viagem iv join carro ic2 on iv.carro_idcarro = ic2.idcarro where ic2.motorista_idmotorista = c2.motorista_idmotorista) as qtd_viagens from avaliacao av join mensagem m2 on av.mensagem_idmensagem = m2.idmensagem join viagem v on av.idavaliacao = v.avaliacao_idavaliacao join carro c2 on v.carro_idcarro = c2.idcarro join motorista m3 on c2.motorista_idmotorista = m3.idmotorista join auth_user a on m3.usuario_idusuario = a.id group by a.id, a.first_name, a.last_name, c2.motorista_idmotorista order by media desc, qtd_viagens desc ) as tab where tab.media > (select avg(wav.nota) from avaliacao wav) fetch first 10 rows only"
    with connection.cursor() as cursor:
            cursor.execute(sql_string)
            row = cursor.fetchall()
            print(row)
    return render(request, 'top_motoristas.html', {'row':row})


def media_motorista(request):
    sql_string="SELECT * FROM (SELECT au.first_name as nome, placa, media FROM (SELECT c.placa as placa, round(CAST(avg(a.nota) as numeric), 2) as media, c.motorista_idmotorista as motorista FROM public.viagem v INNER JOIN public.avaliacao a on v.avaliacao_idavaliacao = a.idavaliacao INNER JOIN public.carro c on c.idcarro = v.carro_idcarro GROUP BY placa, motorista ) as query1 INNER JOIN motorista m ON m.idmotorista = motorista INNER JOIN public.auth_user au on au.id = m.usuario_idusuario GROUP BY nome, placa, media, motorista ) as query2 GROUP BY nome, placa, media"
    with connection.cursor() as cursor:
            cursor.execute(sql_string)
            row = cursor.fetchall()
            print(row)
    return render(request, 'media_motoristas.html', {'row':row})

def media_salarial(request):
    sql_string="select au.id as iduser, m.idmotorista, (au.first_name || ' ' || au.last_name) as nome, 'R$ ' || round(CAST(sum(c.preco) as numeric), 2) as total, 'R$ ' || round(CAST((sum(c.preco) * 0.9) as numeric), 2) as pt_motorista, 'R$ ' || round(CAST((sum(c.preco) * 0.1) as numeric), 2) as pt_carona from auth_user au join motorista m on au.id = m.usuario_idusuario left join carro car on m.idmotorista = car.motorista_idmotorista join viagem v on car.idcarro = v.carro_idcarro join custo c on v.custo_idcusto = c.idcusto group by au.id, m.idmotorista;"
    with connection.cursor() as cursor:
            cursor.execute(sql_string)
            row = cursor.fetchall()
            print(row)
    return render(request, 'media_salarial.html', {'row':row})

    
def freq_cidade(request):
    sql_string="SELECT c.idcidade, c.nome, count(1) AS frequencia FROM viagem v JOIN trajeto t on v.trajeto_idtrajeto = t.idtrajeto JOIN cidade c on t.cidade_origem = c.idcidade group by c.idcidade UNION ALL SELECT idcidade, nome, count (1) AS frequencia FROM viagem v JOIN trajeto t on v.trajeto_idtrajeto = t.idtrajeto JOIN cidade c3 on t.cidade_destino = c3.idcidade group by idcidade;"
    with connection.cursor() as cursor:
            cursor.execute(sql_string)
            row = cursor.fetchall()
            print(row)
    return render(request, 'freq_cidade.html', {'row':row})

