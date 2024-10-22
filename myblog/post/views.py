from django.shortcuts import render
#from django.http import HttpResponse
from .models import Autor , Entrada

# Create your views here.

def query(request):
    #pedir todo
    autores=Autor.objects.all()
    return render(request,'post/query.html',{'autores':autores})