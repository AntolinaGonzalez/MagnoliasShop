from django.shortcuts import render
from .models import Favorito
import json
from django.http import HttpResponse 
# Create your views here.

def marcador(request,pk):
    usuario = request.user
    favoritos, created = Favorito.objects.get_or_create(
        user = usuario,
        objecto_id = pk
    )

    datos = {}
    datos['creado']= "Fav creado exitosamente"
    datos['resultado'] = created
    datos['favoritospk']=favoritos.pk

    if not created:
        favoritos.delete()
        print("eliminado")

    if created:
        print("creado")

    return HttpResponse(
        json.dumps(datos),
        content_type = 'aplication/json'
    )

