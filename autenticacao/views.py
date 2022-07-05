from django.shortcuts import render
from django.http import HttpResponse 
from .utils import password_is_valid

def cadastro(request):
    if request.method == "GET":
        # resposta http que renderiza uma página html
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        return HttpResponse(confirmar_senha)

def logar(request):
    return HttpResponse("Você está na página de Login!")