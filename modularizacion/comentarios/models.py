from django.db import models

# Create your models here.
class Comentario(models.Model):
   name=models.CharField(max_length=255,null=False)
   score=models.IntegerField(default=3)
   comentario=models.TextField(max_length=1000,null=True)
   fecha=models.DateField(null=True)
   
def __str__(self):
      return self.name
   
