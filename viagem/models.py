# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


'''
Ainda to pensando como vai ficar isso aqui pq pretendo usar o google maps api
para pegar a distância
'''


class Pais(models.Model):
    nome = models.CharField("País", max_length=30, null=False, blank = False)
    sigla = models.CharField("Sigla", max_length=30, null=False, blank = False)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

        def __str__(self):
            return self.nome


class Estado(models.Model):
    nome = models.CharField("Estado", max_length=30, null=False, blank = False)
    sigla = models.CharField("Sigla", max_length=30, null=False, blank = False)
    pais = models.ForeignKey("Pais", verbose_name="País", null = False, blank= False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

        def __str__(self):
            return self.nome

class Cidade(models.Model):
    nome = models.CharField("Estado", max_length=30, null=False, blank = False)
    estado = models.ForeignKey("Estado", verbose_name="Estado", null = False, blank= False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

        def __str__(self):
            return self.nome

class Trajeto(models.Model):
    cidade_destino = models.ForeignKey("Cidade", related_name= 'cidade_trajeto_destino', verbose_name="Cidade Destino", null = False, blank= False, on_delete=models.CASCADE)
    cidade_origem = models.ForeignKey("Cidade",  related_name= 'cidade_trajeto_origem', verbose_name="Cidade Origem", null = False, blank= False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Trajeto"
        verbose_name_plural = "Trajetos"


class Viagem(models.Model):
    carro = models.ForeignKey("carros.Carro", verbose_name="Carro", null=False, blank=False, on_delete=models.CASCADE)
    passageiro = models.ForeignKey("contas.Usuario", verbose_name="Passageiro", null=False, blank=False, on_delete=models.CASCADE)
    trajeto = models.ForeignKey("Trajeto", verbose_name="Tipos", null=False, blank=False, on_delete=models.CASCADE)
    custo = models.DecimalField("Custo", null=False, blank=False, max_digits=8,  decimal_places=2)
    vagas = models.IntegerField("Vagas")

    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"
