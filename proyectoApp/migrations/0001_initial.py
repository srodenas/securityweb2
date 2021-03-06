# Generated by Django 4.0 on 2022-01-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('fecha_eliminación', models.DateField(auto_now_add=True, verbose_name='Fecha de eliminación')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Cliente')),
                ('apellido', models.CharField(max_length=150, verbose_name='Apellidos del Clinte')),
                ('email', models.EmailField(max_length=200, verbose_name='Email del Cleinte')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
