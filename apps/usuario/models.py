from django.db import models
import datetime

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=30)
	documento = models.CharField(max_length=30)
	correo = models.EmailField()
	celular = models.CharField(max_length=10)
	telefono = models.CharField(max_length=16)
	direccion = models.CharField(max_length=70)
	departamento = models.CharField(max_length=20)
	ciudad = models.CharField(max_length=30)
	fecha_nacimiento = models.DateField(max_length=30)
	genero = models.CharField(max_length=30)
	estado_civil = models.CharField(max_length=30)
	ocupacion = models.CharField(max_length=30)

	def __str__(self):
		return 'Nombre: ' + self.nombre + ' Doc: ' + self.documento

class Notificacion(models.Model):
	correo_electronico = models.BooleanField()
	mensaje_texto = models.BooleanField()
	llamada_telefonica = models.BooleanField()
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
	fecha_notificacion = models.DateField(default=datetime.date.today)

class Puntos(models.Model):
	puntos = models.CharField(max_length=999)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha_puntos = models.DateField(default=datetime.date.today)

class Compras(models.Model):
	compra = models.CharField(max_length=90)
	tipo = models.CharField(max_length=90)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha_compra = models.DateField(default=datetime.date.today)

class Lista_Favorito(models.Model):
	nombre = models.CharField(max_length=90)
	tipo = models.CharField(max_length=90)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha_lista = models.DateField(default=datetime.date.today)

class Carrito(models.Model):
	nombre = models.CharField(max_length=90)
	tipo = models.CharField(max_length=90)
	valor = models.CharField(max_length=999)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha_carrito = models.DateField(default=datetime.date.today)

