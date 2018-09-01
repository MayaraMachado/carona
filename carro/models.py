from django.db import models
from usuario_tipo.models import Motorista


class Carro(models.Model):
    idcarro = models.IntegerField(primary_key=True)
    placa = models.CharField(unique=True, max_length=8)
    cor = models.CharField(max_length=45)
    tipo_idtipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='tipo_idtipo')
    motorista_idmotorista = models.ForeignKey(Motorista, models.DO_NOTHING, db_column='motorista_idmotorista')

    class Meta:
        managed = False
        db_table = 'carro'
        unique_together = (('idcarro', 'motorista_idmotorista'),)


class Tipo(models.Model):
    idtipo = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo'



class Combustivel(models.Model):
    idcombustivel = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    preco = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'combustivel'

class TipoTemCombustivel(models.Model):
    idcombustivel = models.ForeignKey(Combustivel, models.DO_NOTHING, db_column='idcombustivel', unique=False, primary_key=True)
    idtipo = models.ForeignKey(Tipo, models.DO_NOTHING, db_column='idtipo')

    class Meta:
        managed = False
        db_table = 'tipo_tem_combustivel'
        unique_together = ( 'idtipo',)