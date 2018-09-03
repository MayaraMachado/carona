from django.shortcuts import render
from .forms import *
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

