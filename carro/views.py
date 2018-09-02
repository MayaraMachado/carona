from django.shortcuts import render

def index(request):
    context ={
        'titulo_variavel': 'Carona'
    }
    return render(request, 'index.html', context)