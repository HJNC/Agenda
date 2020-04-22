from django.db import models

#colocar usuario
from django.contrib.auth.models import User


# Create your models here.

#criar classes para o banco de dados

class Evento(models.Model):
    #Vai ser depositados os caracteres no banco de dados, max_length é o tamanho maximo de caracteres
    titulo= models.CharField(max_length=100)

    #aceita ficar em branco ou ser nulo
    descricao= models.TextField(blank=True, null=True)

    data_evento= models.DateTimeField(verbose_name='Data do evento')

    #grava a data e hora automaticamente
    data_criacao= models.DateTimeField(auto_now=True, verbose_name='Data de criação')

    #criando o usuario
    #se o usuario for deletado, apaga-se todos os dados
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #nome da tabela
    class Meta:
        db_table = 'evento'

    #titulo do lembrete
    def __str__(self):
            return self.titulo
