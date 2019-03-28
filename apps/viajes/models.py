from django.db import models
import datetime
# Create your models here.

class Vuelo(models.Model):
	desde = models.CharField(max_length=30)
	hasta = models.CharField(max_length=30)
	cuando_viaja = models.CharField(max_length=30)
	cuando_vuelve = models.CharField(max_length=999)
	numeroAdulto = ((1,'1'),(2,'2'),(1,'1'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_adultos = models.IntegerField(choices=numeroAdulto, default=1)
	numeroNinos = ((1,'1'),(2,'2'),(1,'1'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_ninos = models.IntegerField(choices=numeroNinos, default=1)
	fecha_vuelo = models.DateField(default=datetime.date.today)

class Plan(models.Model):
	desde = models.CharField(max_length=30)
	hasta = models.CharField(max_length=30)
	cuando_viaja = models.DateField(default=datetime.date.today)
	cuando_vuelve = models.DateField(default=datetime.date.today)
	numeroHab = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_habitaciones = models.IntegerField(choices=numeroHab, default=1)
	numeroAdulto = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_adultos = models.IntegerField(choices=numeroAdulto, default=1)
	numeroNinos = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_ninos = models.IntegerField(choices=numeroNinos, default=1)
	incluye = (('si','si'),('no','no'))
	incluye_equipaje = models.CharField(choices=incluye, default='no', max_length=40)
	fecha_plan = models.DateField(default=datetime.date.today)

class Hotel(models.Model):
	donde = models.CharField(max_length=30)
	cuando_llegas = models.CharField(max_length=30)
	cuando_sales = models.CharField(max_length=30)
	numeroHab = ((1,'1'),(2,'2'),(1,'1'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_habitaciones = models.IntegerField(choices=numeroHab, default=1)
	numeroAdulto = ((1,'1'),(2,'2'),(1,'1'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_adultos = models.IntegerField(choices=numeroAdulto, default=1)
	numeroNinos = ((1,'1'),(2,'2'),(1,'1'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'))
	numero_ninos = models.IntegerField(choices=numeroNinos, default=1)
	fecha_hotel = models.DateField(default=datetime.date.today)

class Auto(models.Model):
	recoger = models.CharField(max_length=30)
	entregar = models.CharField(max_length=30)
	cuando_llegas = models.DateField(default=datetime.date.today)
	hora = (('por_mañana','por la mañana'),('por_tarde','por la tarde'),('por_noche','por la noche'))
	hora_salida = models.CharField(choices=hora, default=1, max_length=40)
	cuando_entregas = models.DateField(default=datetime.date.today)
	horaEntrega = (('por_mañana','por la mañana'),('por_tarde','por la tarde'),('por_noche','por la noche'))
	hora_entrega = models.CharField(choices=horaEntrega, default=1, max_length=40)
	fecha_auto = models.DateField(default=datetime.date.today)

class Actividad(models.Model):
	hacia_donde = models.CharField(max_length=30)
	cuando_llegas = models.DateField(default=datetime.date.today)
	cuando_regresas = models.DateField(default=datetime.date.today)
	fecha_actividad = models.DateField(default=datetime.date.today)

	


