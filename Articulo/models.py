from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    GLN = models.CharField(max_length=80)
    price = models.FloatField()

