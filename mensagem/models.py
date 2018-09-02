<<<<<<< HEAD
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
=======
from django.db import models
from conta.models import AuthUser


class Avaliacao(models.Model):
    idavaliacao = models.IntegerField(primary_key=True)
    nota = models.FloatField()
    mensagem_idmensagem = models.ForeignKey('Mensagem', models.DO_NOTHING, db_column='mensagem_idmensagem')

    class Meta:
        managed = False
        db_table = 'avaliacao'



class Conversa(models.Model):
    idconversa = models.IntegerField(primary_key=True)
    mensagem_idmensagem = models.IntegerField()
    viagem_idviagem = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conversa'
        unique_together = (('idconversa', 'mensagem_idmensagem'),)


class Mensagem(models.Model):
    idmensagem = models.IntegerField(primary_key=True)
    mensagem = models.TextField(blank=True, null=True)
    conversa_idconversa = models.IntegerField()
    usuario_idusuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'mensagem'
>>>>>>> 8de7ee5ee40b90b103d254cf169f2f6f70e8a33b
