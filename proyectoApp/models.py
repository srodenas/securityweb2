from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
''' 
Para PSP 2021/2022
@Santi
# ------Todos nuestros modelos, deben heredar en base de models.models----
* En fecha_creación y fecha_eliminación
    * auto_now lo ponemos a False, para que no deje constancia cada vez que modifico
un modelo. 
    * auto_now_add lo ponemos a True, para que deje constancia de la fecha de creación
cuando un modelo es creado.
* En fecha_modificación
    * auto_now lo ponemos a True
    * auto_now_add lo ponemos a False
* Será un modelo abstracto para que el resto heredan del mismo sin tener
que crear una tabla en la BBDD.
'''
class ModeloBase(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now = True, auto_now_add = False)
    fecha_eliminación = models.DateField('Fecha de eliminación', auto_now = False, auto_now_add = True)

    class Meta:
        abstract = True

'''
* Hereda de modeloBase
'''
class Cliente(ModeloBase):
    nombre = models.CharField('Nombre del Cliente', max_length = 100, unique = True)
    apellido = models.CharField('Apellidos del Clinte', max_length =150)
    email = models.EmailField('Email del Cleinte',max_length=200)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    #Cómo queremos ver los datos de las categorías.
    def __str__(self):
        return self.nombre


class Articulo(ModeloBase):
    descripcion = models.CharField('Descripcion del artículo', max_length=200)
    precio = models.CharField('Precio del artículo', max_length= 5)
    
    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        
    def __str__(self):
        return self.descripcion