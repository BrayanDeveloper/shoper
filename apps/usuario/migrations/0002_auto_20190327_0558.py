# Generated by Django 2.1.7 on 2019-03-27 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_electronico', models.BooleanField()),
                ('mensaje_texto', models.BooleanField()),
                ('llamada_telefonica', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='departamento',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario'),
        ),
    ]
