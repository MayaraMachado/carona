# Generated by Django 2.0.6 on 2018-09-02 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('idcidade', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'cidade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Custo',
            fields=[
                ('idcusto', models.IntegerField(primary_key=True, serialize=False)),
                ('preco', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'custo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idestado', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('sigla', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idpais', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('sigla', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trajeto',
            fields=[
                ('idtrajeto', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'trajeto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('idviagem', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'viagem',
                'managed': False,
            },
        ),
    ]
