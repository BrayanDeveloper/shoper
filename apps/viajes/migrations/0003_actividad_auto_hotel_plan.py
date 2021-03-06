# Generated by Django 2.1.7 on 2019-03-27 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0002_auto_20190327_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hacia_donde', models.CharField(max_length=30)),
                ('cuando_llegas', models.DateField(default=datetime.date.today)),
                ('cuando_regresas', models.DateField(default=datetime.date.today)),
                ('fecha_actividad', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recoger', models.CharField(max_length=30)),
                ('entregar', models.CharField(max_length=30)),
                ('cuando_llegas', models.DateField(default=datetime.date.today)),
                ('hora_salida', models.CharField(choices=[('por_mañana', 'por la mañana'), ('por_tarde', 'por la tarde'), ('por_noche', 'por la noche')], default=1, max_length=40)),
                ('cuando_entregas', models.DateField(default=datetime.date.today)),
                ('hora_entrega', models.CharField(choices=[('por_mañana', 'por la mañana'), ('por_tarde', 'por la tarde'), ('por_noche', 'por la noche')], default=1, max_length=40)),
                ('fecha_auto', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donde', models.CharField(max_length=30)),
                ('cuando_llegas', models.CharField(max_length=30)),
                ('cuendo_sales', models.CharField(max_length=30)),
                ('numero_habitaciones', models.IntegerField(choices=[(1, '1'), (2, '2'), (1, '1'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1)),
                ('numero_adultos', models.IntegerField(choices=[(1, '1'), (2, '2'), (1, '1'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1)),
                ('numero_ninos', models.IntegerField(choices=[(1, '1'), (2, '2'), (1, '1'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1)),
                ('fecha_hotel', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.CharField(max_length=30)),
                ('hasta', models.CharField(max_length=30)),
                ('cuendo_viaja', models.CharField(max_length=30)),
                ('cuando_vuelve', models.CharField(max_length=999)),
                ('numero_habitaciones', models.IntegerField(choices=[(1, '1'), (2, '2'), (1, '1'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1)),
                ('numero_adultos', models.IntegerField(choices=[(1, '1'), (2, '2'), (1, '1'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1)),
                ('numero_ninos', models.IntegerField(choices=[(1, '1'), (2, '2'), (1, '1'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1)),
                ('incluye_equipaje', models.CharField(choices=[('si', 'si'), ('no', 'no')], default='no', max_length=40)),
                ('fecha_plan', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
