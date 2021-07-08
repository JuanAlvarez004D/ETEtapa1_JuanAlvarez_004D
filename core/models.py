from django.db import models

# Create your models here.

class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True)
    nombrePais = models.CharField(max_length=50)
    def __str__(self):
        return self.nombrePais

class Usuario(models.Model):
    RutUsuario = models.CharField(max_length=10, primary_key=True, verbose_name='Rut del Colaborador')
    image = models.ImageField(upload_to='images/', null=True)
    NombreCom = models.CharField(max_length=50, verbose_name='Nombre Completo' )
    Telefono = models.CharField(max_length=12, verbose_name= 'Teléfono')
    Direccion = models.CharField(max_length=60, verbose_name='Dirección')
    email = models.CharField(max_length=70, verbose_name='Email')
    idPais = models.ForeignKey('Pais', on_delete=models.SET_NULL, null=True, blank=False)
    password = models.CharField(max_length=8, null=True, blank=False) 

    def __str__(self):
        return self.RutUsuario

