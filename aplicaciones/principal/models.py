from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.template import defaultfilters
from django.shortcuts import reverse

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
    id = models.AutoField(primary_key = True)
    cat= models.ForeignKey(Category, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    precio = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    publico = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse ('principal:producto', kwargs={
            'pk':self.id
        })
    
    def get_addToCar_url(self):
        return reverse ('principal:addToCart', kwargs={
            'pk':self.id
        })
    def get_removeFromCar_url(self):
        return reverse ('principal:removeFromCart', kwargs={
            'pk':self.id
        })

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Clothing, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default= False)
    def __str__(self):
        return self.item.nombre

    def getTotalPrice(self):
        return self.quantity * self.item.precio

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items= models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default= False)
    def __str__(self):
        return self.user.username

    def getTotalPrice(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.getTotalPrice()
        return total 