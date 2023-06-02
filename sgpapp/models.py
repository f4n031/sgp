from django.db import models


class Cadastro(models.Model):
    # Informações Pessoais
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    ZONA_CHOICES = (
        ('U', 'Zona Urbana'),
        ('R', 'Zona Rural'),
    )
    # Endereço
    logradouro = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    zona = models.CharField(max_length=10, choices=ZONA_CHOICES)
    bairro = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=50, blank=True)
    municipio = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=9, blank=True)

    # Formação
    ESCOLADIRDADE_CHOICES = (
        ('F', 'Ensino Fundamental'),
        ('M', 'Ensino Médio'),
        ('S', 'Ensino Superior'),
    )
    escolaridade = models.CharField(max_length=10, choices=ESCOLADIRDADE_CHOICES)
    formacao = models.CharField(max_length=100, default='', blank=True)
    instituicao = models.CharField(max_length=100, blank=True)

    # Lotação
    LOCAL_CHOICES = (
        ('S', 'SEMED'),
        ('B', 'E.M.E.F Brejo Grande do Araguaia'),
        ('XV', 'E.M.E.F XV de Novembro'),
        ('C', 'E.M.E.F Cilira Vieira'),
        ('F', 'E.M.E.I Felicidade de Brito'),
        ('M', 'E.M.E.I Dona Maria de Nazaré'),
        ('S', 'E.M.E.I.F Silvana Moura'),
        ('J', 'E.M.E.I.F Joventina'),
        ('N', 'E.M.E.I.F Nossa Senhora da Penha'),
        ('SS', 'E.M.E.I.F São José'),
        ('P', 'E.M.E.I.F Padre Cicero'),
        ('SA', 'E.M.E.I.F Sawarapy Suruí'),
        ('D', 'E.M.E.I.F Dom Bosco'),
    )
    VINCULO_CHOICES = (
        ('E', 'Efetivo'),
        ('T', 'Temporário'),
    )
    cargo = models.CharField(max_length=50, blank=True)
    funcao = models.CharField(max_length=50, blank=True)
    vinculo = models.CharField(max_length=15, choices=VINCULO_CHOICES)
    local = models.CharField(max_length=10, choices=LOCAL_CHOICES)
    obs = models.TextField(blank=True)
    lotacao = models.CharField(max_length=100, blank=True)

    # Dados Bancários
    banco = models.CharField(max_length=50, blank=True)
    agencia = models.CharField(max_length=10, blank=True)
    conta = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
