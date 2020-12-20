from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    numero = models.CharField(max_length=20, null=True, default='')
    def __str__(self):
        return self.numero

class Articulo(models.Model):
    GLN = models.CharField(max_length=80)
    precio = models.FloatField()
    pedido = models.ForeignKey('pedido', null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.GLN, self.precio


