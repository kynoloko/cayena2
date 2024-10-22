from django.db import models
from datetime import date

# Create your models here.

class Autor(models.Model):
    name=models.CharField(max_length=200)
    emal=models.EmailField()
    
    def __str__(self):
        return self.name
    
class Entrada(models.Model):
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    cabecera=models.CharField(max_length=255)
    cuerpotexto=models.TextField()
    fecha=models.DateField(default=date.today)
    promedio=models.IntegerField(default=5)
    
    def __str__(self):
        return self.cabecera