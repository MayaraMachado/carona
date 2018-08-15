# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin



class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Usuario', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                    'Informe um nome de usuurio valido. '
                    'Este valor deve conter apenas letras, numeros '
                    'e os caracteres: @/./+/-/_ .'
                    , 'invalid'
            )
        ], help_text = 'Um nome curto que sera usado para identifica-lo de forma unica na plataforma'
    )
    nome = models.CharField('Nome', max_length=50, blank = False)
    sobrenome = models.CharField('Sobrenome', max_length=100, blank = True )
    email = models.EmailField('Email', blank = False, unique=True)
    is_active = models.BooleanField(" Esta ativo ", default=True)
    is_staff = models.BooleanField('Equipe', default=True)

    objects = UserManager()

    USERNAME_FIELD="username"
    REQUIRED_FIELDS=["email"]

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

        def __str__(self):
            return self.username

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome+" "+self.sobrenome


class Telefone(models.Model):
    numero = models.CharField("Telefone", max_length=15,blank=False, validators=[
            validators.RegexValidator(
                re.compile('\({0,1}\d{2}\){0,1}\d{3,4}-{0,1}\d{3,4}$'),
                    'Informe um número de telefone válido. '
                    'Este valor deve conter apenas numeros no formato (ddd)xxxxx-xxxx.'
                    , 'invalid'
            )])
    usuario = models.ForeignKey('Usuario', verbose_name = "Usuário", blank = False, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

        def __str__(self):
            return self.numero

    