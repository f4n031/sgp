from django.db import models


class Cadastro(models.Model):
    # Informações Pessoais
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    # Endereço
    logradouro = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    zona = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=50, blank=True)
    municipio = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=9, blank=True)

    # Formação
    escolaridade = models.CharField(max_length=50, blank=True)
    formacao = models.CharField(max_length=100, default='', blank=True)
    instituicao = models.CharField(max_length=100, blank=True)

    # Lotação
    cargo = models.CharField(max_length=50, blank=True)
    funcao = models.CharField(max_length=50, blank=True)
    vinculo = models.CharField(max_length=50, blank=True)
    local = models.CharField(max_length=100, blank=True)
    obs = models.TextField(blank=True)
    lotacao = models.CharField(max_length=100, blank=True)

    # Dados Bancários
    banco = models.CharField(max_length=50, blank=True)
    agencia = models.CharField(max_length=10, blank=True)
    conta = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
