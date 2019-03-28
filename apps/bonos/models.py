from django.db import models
import datetime
# Create your models here.

class Bono(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='static/img')
	puntos = models.CharField(max_length=999)
	fecha_bono = models.DateField(default=datetime.date.today)