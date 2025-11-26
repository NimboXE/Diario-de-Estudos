from django.db import models

## Importando o AbstractUser para a criação do usuario ##
from django.contrib.auth.models import AbstractUser

# Create your models here.

## Classe do usuário (Como ela herda do AsbtractUser, já contém username, email e password) ##
class Usuario(AbstractUser):
    nome = models.CharField(max_length=50, null=False, blank=False)
    informacoes = models.TextField(null=False, blank=True)

## Classe das Matérias (Matemática, etc.) ##
class Materia(models.Model):
    nome = models.CharField(max_length=50, primary_key=True, null=False, blank=False)

## Relacionamento entre Usuário e Matéria, permitindo a verificação entre as duas ##
class RelacionamentoUsuarioMaterias(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False, blank=False)

## Classe para as atividades do usuario. Elas pertencem a um aluno e a uma matéria ##
class Atividade(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=True)
    descricao = models.TextField(null=False, blank=False)
    situacao = models.CharField(null=False, blank=False, default="Pendente")
    data_de_entrega = models.DateField(null=False, blank=True)
    materia_fk = models.ForeignKey(Materia, on_delete=models.CASCADE)
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)

## Classe para o plano de estudos que a IA vai gerar para as atividades. O plano pertence a um usuário, atividade e matéria ##
class PlanoDeEstudos(models.Model):
    plano = models.TextField(null=False, blank=False)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

## Classe para as anotações do usuário ##
class Anotacao(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    hora_de_criacao = models.DateTimeField(auto_now_add=True)