# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Motorista(models.Model):

    cnh = models.CharField('CNH', max_length = 15, blank = False)
    usuario = models.ForeignKey('contas.Usuario', on_delete = models.CASCADE, blank= False)

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'

        def __str__(self):
            return self.usuario.nome

    
# class Passageiro(models.Model):

#     usuario = models.ForeingKey('contas.Usuario', on_delete=models.CASCADE, blank=False)

    
