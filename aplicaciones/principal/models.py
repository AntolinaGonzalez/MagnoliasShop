from django.db import models
from django import forms


# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=150)
    contra = models.CharField(max_length=150)
    confir = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    def __str__(self):              
        return self.name

class HeroSeccion(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField( null=True, blank=True)
    name = models.CharField(max_length=50)
    arts = models.CharField(max_length=50)
    descuento = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class BannerSection(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField( null=True, blank=True)
    nombre = models.CharField(max_length=50)

class Persona(models.Model):
    publico = models.CharField( max_length=50, primary_key = True)

class AsideImage(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(null=True, blank=True)
    nombre= models.CharField(max_length=50)
    frase= models.CharField(max_length=50)
    publico = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField( max_length=50, primary_key = True)


class Clothing(models.Model):
    #Aid= models.ForeignKey(AsideImage,default=1, verbose_name="Aside", on_delete=models.SET_DEFAULT)
    cat= models.ForeignKey(Category, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    precio = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    publico = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

