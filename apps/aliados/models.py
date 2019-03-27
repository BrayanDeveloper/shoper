from django.db import models
import datetime
# Create your models here.
class Aliado(models.Model):

	def thumbnail(self):
		return '<img src="/photos/%s" width="50" height="50"/>'%(self.imagen)

	thumbnail.allow_tags = True

	nombre = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='photos')
	descripcion = models.CharField(max_length=30)
	fecha_aliado = models.DateField(default=datetime.date.today)