# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


 |- Usuario
        |-cpf
        |-email
        |-nome
        |-sobrenome
        |-username
        |-senha
    |-Telefone 
        |-numero
        |-cpf** Chave estrangeira de usuário

class Usuario(models.Model):
    username = models.CharField("Username")