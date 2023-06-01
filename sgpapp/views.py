from django.shortcuts import render, redirect
from .forms import SignUpForm


def index(request):
    return render(request, 'sgp/index.html')


def gerenciar(request):
    return render(request, 'sgp/gerenciar.html')


def signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = SignUpForm()
    return render(request, 'sgp/signup.html', {'form': form})
