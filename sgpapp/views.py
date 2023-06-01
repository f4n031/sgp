from django.shortcuts import render


def index(request):
    return render(request, 'sgp/index.html')


def cadastro(request):
    return render(request, 'sgp/cadastro.html')


def gerenciar(request):
    return render(request, 'sgp/gerenciar.html')
# Create your views here.
