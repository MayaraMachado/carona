from django.db import models
from usuario_tipo.models import Passageiro
from carro.models import Carro
from mensagem.models import Avaliacao

class Custo(models.Model):
    idcusto = models.IntegerField(primary_key=True)
    preco = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custo'

    def __str__(self):
        return str(self.preco)

class Cidade(models.Model):
    idcidade = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    estado_idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado_idestado')

    class Meta:
        managed = False
        db_table = 'cidade'

    def __str__(self):
        return self.nome


class Estado(models.Model):
    idestado = models.IntegerField(primary_key=True)
    idpais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='idpais')
    nome = models.CharField(max_length=45)
    sigla = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'estado'
    
    def __str__(self):
        return self.nome

class Pais(models.Model):
    idpais = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    sigla = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pais'
    
    def __str__(self):
        return self.nome


class Trajeto(models.Model):
    idtrajeto = models.IntegerField(primary_key=True)
    cidade_origem = models.ForeignKey(Cidade, models.DO_NOTHING,related_name="cidade1" , db_column='cidade_origem')
    cidade_destino = models.ForeignKey(Cidade, models.DO_NOTHING, related_name="cidade2", db_column='cidade_destino')

    class Meta:
        managed = False
        db_table = 'trajeto'


    def __str__(self):
        return self.cidade_origem.nome+" - "+self.cidade_destino.nome
class Viagem(models.Model):
    idviagem = models.IntegerField(primary_key=True)
    custo_idcusto = models.ForeignKey(Custo, models.DO_NOTHING, db_column='custo_idcusto')
    trajeto_idtrajeto = models.ForeignKey(Trajeto, models.DO_NOTHING, db_column='trajeto_idtrajeto')
    passageiro_idpassageiro = models.ForeignKey(Passageiro, models.DO_NOTHING, db_column='passageiro_idpassageiro')
    carro_idcarro = models.ForeignKey(Carro, models.DO_NOTHING, db_column='carro_idcarro')
    avaliacao_idavaliacao = models.ForeignKey(Avaliacao, models.DO_NOTHING, db_column='avaliacao_idavaliacao')

    class Meta:
        managed = False
        db_table = 'viagem'
        unique_together = (('idviagem', 'custo_idcusto', 'trajeto_idtrajeto'),)

    def __str__(self):
        return str(self.idviagem)