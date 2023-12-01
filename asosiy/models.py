from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yoshi = models.PositiveSmallIntegerField()
    kasbi = models.CharField(max_length=30)
    egasi = models.ForeignKey(User ,on_delete=models.CASCADE, null=True)

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=30)
    sana = models.DateTimeField()
    mavzu = models.CharField(max_length=150)
    matn = models.CharField(max_length=500)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
