from django.shortcuts import render
from django.http import HttpResponse 

def cadastro(request):
    if request.method == "GET":
        # resposta http que renderiza uma página html
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        return HttpResponse(f'{usuario} e {email}')

def logar(request):
    return HttpResponse("Você está na página de Login!")