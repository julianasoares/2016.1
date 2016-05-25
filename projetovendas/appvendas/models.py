from django.db import models

# Create your models here.

class Unidade(models.Model):
    descricao=models.CharField("Descrição",max_length=100)
    sigla=models.CharField("Sigla",max_length=5)

class Cargo(models.Model):
    descricao=models.CharField("Descrição",max_length=150)

class Pessoa(models.Model):
    nome=models.CharField("Nome",max_length=255)
    email=models.EmailField("E-Mail",max_length=200)
    telefone=models.CharField("Telefone",max_length=20)

class Cliente(Pessoa):
    endereco=models.CharField("Endereço",max_length=255)

class Funcionario(Pessoa):
    matricula=models.CharField("Matrícula",max_length=10)
    cargo=models.ForeignKey(Cargo,on_delete=models.PROTECT,verbose_name="Cargo")

class Produto(models.Model):
    descricao=models.CharField("Descrição",max_length=255)
    valorUnitario=models.DecimalField("Valor Unitário",max_digits=10,decimal_places=2)
    unidade=models.ForeignKey(Unidade,on_delete=models.PROTECT,verbose_name="Unidade")