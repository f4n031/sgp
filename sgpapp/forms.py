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
            'banco': 'Banco',
            'agencia': 'Agência',
            'conta': 'Conta',
            'data_admissao': 'Data de Admissão',
            'data_inicio': 'Data de Início',
            'data_saida': 'Data de Saída',
            'data_nascimento': 'Data de Nascimento',
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
