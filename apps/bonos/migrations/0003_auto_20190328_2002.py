# Generated by Django 2.1.7 on 2019-03-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonos', '0002_auto_20190327_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bono',
            name='imagen',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
