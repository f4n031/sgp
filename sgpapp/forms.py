from django import forms
from .models import Cadastro


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'sexo': 'Sexo',
            'rg': 'RG',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'email': 'Email',
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'zona': 'Zona',
            'bairro': 'Bairro / Vila',
            'estado': 'Estado',
            'municipio': 'Município',
            'cep': 'CEP',
            'escolaridade': 'Escolaridade',
            'formacao': 'Formação',
            'instituicao': 'Instituição',
            'cargo': 'Cargo',
            'funcao': 'Função',
            'vinculo': 'Vínculo',
            'local': 'Local',
            'obs': 'Observações',
            'lotacao': 'Lotação',
            'banco': 'Banco',
            'agencia': 'Agência',
            'conta': 'Conta'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].required = True
        self.fields['sexo'].required = True
        self.fields['rg'].required = True
        self.fields['cpf'].required = True
        self.fields['telefone'].required = True
        self.fields['email'].required = True
        self.fields['zona'].required = False
        self.fields['zona'].required = False


def save(self, *args, **kwargs):
    # definir o valor completo do campo vinculo_completo
    if self.vinculo == 'E':
        self.vinculo_completo = 'Efetivo'
    elif self.vinculo == 'T':
        self.vinculo_completo = 'Temporário'

    super().save(*args, **kwargs)
