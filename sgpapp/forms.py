from django import forms
from .models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].required = True
        self.fields['sexo'].required = True
        self.fields['rg'].required = True
        self.fields['cpf'].required = True
        self.fields['telefone'].required = True
        self.fields['email'].required = True