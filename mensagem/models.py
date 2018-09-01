from django.db import models


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

    class Meta:
        managed = False
        db_table = 'mensagem'
