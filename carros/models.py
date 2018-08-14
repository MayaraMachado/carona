# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import validators
import re
from django.db import models

# 3- Carros
#     |-Combustivel
#         |-nome
#         |-preco
#     |-Tipo
#         |-marca
#         |-modelo
#     |-tipo_tem_combustivel
#         |-combustivel**
#         |-tipo**
#     |-Carro
#         |-placa
#         |-cor
#         |-motorista**
#         |-tipo**

class Combustivel(models.Model):
    nome = models.CharField('Combustível', max_length=40, blank = False, null = False)
    preco = models.DecimalField('Preço', blank = False, null = False, decimal_places=2, max_digits=5)

    class Meta:
        verbose_name = 'Nome'
        verbose_name_plural = 'Nomes'

        def __str__(self):
            return self.nome

class Marca(models.Model):
    marca_nome = models.CharField('Marca', max_length=40, blank = False, null = False)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.marca


class Modelo(models.Model):
    modelo_nome = models.CharField('Modelo', max_length=40, blank = False, null = False)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelo'

    def __str__(self):
        return self.modelo

class Tipo(models.Model):
    marca = models.ForeignKey('Marca', verbose_name='Marca', blank = False, null = False, on_delete=models.CASCADE)
    modelo = models.ForeignKey('Modelo', verbose_name='Modelo', blank = False, null = False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tipo de carro"
        verbose_name_plural = "Tipos de carros"

        def __str__(self):
            return self.modelo.modelo_nome+ " - "+self.marca.marca_nome

class tipo_tem_combustivel(models.Model):
    tipo =  models.ForeignKey('Tipo', verbose_name='Tipo', blank = False, null = False, on_delete=models.CASCADE)
    combustivel =  models.ForeignKey('Combustivel', verbose_name='Combustivel', blank = False, null = False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tipo vs Combustivel"
        verbose_name_plural = "Tipo vs Combustivel"

        def __str__(self):
            return self.tipo+ " - "+self.combustivel

class Carro(models.Model):

    COR_ESCOLHA = (
        ('amarelo', 'Amarelo'),
        ('vermelho', 'Vermelho'),
        ('azul', 'Azul'),
        ('preto', 'Preto'),
        ('branco', 'branco'),
    )

    placa = models.CharField('Placa', max_length= 8, blank = False, null=False,unique=True, validators=[
            validators.RegexValidator(
                '\w{4}\d{4}',
                'Insira um valor de placa válido',
                'invalid'
            )
    ])
    cor = models.CharField('Cor', choices = COR_ESCOLHA, null = False, blank = False, max_length=10)
    motorista = models.ForeignKey('usuario_tipos.Motorista', verbose_name="Motorista", blank = False, null=False, on_delete=models.CASCADE)
    tipo = models.ForeignKey('Tipo', verbose_name = 'Tipo do carro', blank = False, null = False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

        def __str__(self):
            return self.placa