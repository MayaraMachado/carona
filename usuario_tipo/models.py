from django.db import models
from conta.models import Usuario



class Motorista(models.Model):
    idmotorista = models.IntegerField(primary_key=True)
    cnh = models.IntegerField(unique=True)
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'motorista'


class Passageiro(models.Model):
    idpassageiro = models.IntegerField(primary_key=True)
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'passageiro'