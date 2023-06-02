from django.shortcuts import render, redirect, get_object_or_404
from .forms import CadastroForm
from .models import Cadastro



def index(request):
    return render(request, 'sgp/index.html')


def gerenciar(request):
    return render(request, 'sgp/gerenciar.html')


def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            form = CadastroForm()
    return render(request, 'sgp/cadastro.html', {'form': form})


def lista_servidores(request):
    servidores = Cadastro.objects.order_by('nome')  # Ordena os servidores por nome em ordem alfabética
    total_registros = servidores.count()  # Obtém o total de registros

    return render(request, 'sgp/lista_servidores.html', {'servidores': servidores, 'total_registros': total_registros})


def detalhar_servidor(request, id):
    servidor = get_object_or_404(Cadastro, id=id)
    return render(request, 'sgp/detalhar_servidor.html', {'servidor': servidor})

def editar_servidor(request, servidor_id):
    servidor = get_object_or_404(Cadastro, id=servidor_id)
    if request.method == 'POST':
        form = CadastroForm(request.POST, instance=servidor)
        if form.is_valid():
            form.save()
            return redirect('lista_servidores')
    else:
        form = CadastroForm(instance=servidor)
    return render(request, 'sgp/editar_servidor.html', {'form': form})


def apagar_servidor(request, servidor_id):
    servidor = get_object_or_404(Cadastro, id=servidor_id)
    if request.method == 'POST':
        servidor.delete()
        return redirect('lista_servidores')
    return render(request, 'sgp/apagar_servidor.html', {'servidor': servidor})
