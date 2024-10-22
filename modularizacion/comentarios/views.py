from django.shortcuts import render
from django.http import HttpResponse
from .models import Comentario

# Create your views here.
def test(request):
    return HttpResponse('esto funciona de manera coorrecta')

def create(request):
    #comment=Comentario(name='elkin',score=4,comentario='el primer comentario')
    #comment.save()
    comment=Comentario.objects.create(name='pedrito')
    return HttpResponse('ruta para crear modelo')

def delete(request):
    #comment=Comentario.objects.get(id=1)
    #comment.delete()
    Comentario.objects.filter(id=2).delete()
    return HttpResponse('ruta para borrar ')