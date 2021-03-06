"""carona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', index, name='index'),
    path('query',query, name='query' ),
    path('query/busca-sql/<str:sql>',query_sql, name='query_sql' ),
    path('query/busca-cidade', query_cidade, name='query_cidade'),
    path('query/top-motorista', top_motorista, name='top_motorista'),
    path('query/freq_cidade', freq_cidade, name='freq_cidade'),
    path('query/med-motorista', media_motorista, name='media_motorista'),
    path('query/valores', media_salarial, name='media_salarial'),

]
