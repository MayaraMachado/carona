from django.db import models
from conta.models import Usuario, AuthUser



class Motorista(models.Model):
    idmotorista = models.IntegerField(primary_key=True)
    cnh = models.IntegerField(unique=True)
    usuario_idusuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'motorista'


    def __str__(self):
        return self.usuario_idusuario.first_name

class Passageiro(models.Model):
    idpassageiro = models.IntegerField(primary_key=True)
    usuario_idusuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='usuario_idusuario')

    class Meta:
        managed = False
        db_table = 'passageiro'

    def __str__(self):
        return self.usuario_idusuario.first_name