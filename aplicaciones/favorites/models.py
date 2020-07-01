from django.db import models
from django.contrib.auth.models import User
from aplicaciones.principal.models import Clothing
# Create your models here.

class BaseFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favoritos")

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.user.username

class Favorito(BaseFav): 
    objecto = models.ForeignKey(Clothing,on_delete=models.CASCADE, related_name="favoritos" )