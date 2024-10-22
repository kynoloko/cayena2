from django.http import HttpResponse
from django.shortcuts import render


def hola(request): # vista 1

    return HttpResponse("hola mundo esta es cayena")

def simple(request):
    return render(request,'inicio.html',{})

def dinamico(request,name):
    categorias={'uno','dos','tres','cuatro'}
    
    contexto={'name':name,'categorias':categorias}
    return render(request,'dinamico.html',contexto)

def estaticos(request):
    return render(request,'estaticos.html',{})