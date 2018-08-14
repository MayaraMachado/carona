# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models



class Avaliacao(models.Model):
    viagem = models.ForeignKey("viagem.Viagem", verbose_name="Avaliação", null = False, blank = False, on_delete=models.CASCADE)
    nota = models.IntegerField("Nota", blank=False, null="False")
    comentario = models.CharField("Comentário", max_length=280, blank=True, null=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

        def __str__(self):
            return self.nota

class Mensagem(models.Model):
    anexo = models.FileField("Anexo", upload_to="arquivo/mensagem", blank=True, null=True)
    remetente = models.ForeignKey("contas.Usuario", verbose_name="Remetente", null = True, blank=False, on_delete=models.SET_NULL)
    mensagem = models.TextField("Mensagem")
    enviado_em = models.DateTimeField("Enviado em", auto_now_add= True)

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"