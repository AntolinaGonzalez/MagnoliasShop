from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', inicio, name="index"),
    path('login/', login, name="login"),
    path('register/',register, name="register"),
    path('salir/', logout, name="salir"),
    path('cambios/<int:id>/', cambios, name="cambios"),
    path('eliminarPromo/<int:id>/', eliminarPromo, name="eliminar"),
    path('cambiosbanner/<int:id>/', cambiosbanner, name="banner"),
    path('cambiosAside/<int:id>/', cambiosAside, name="cambiosAside"),
    path('eliminarBanner/<int:id>/', eliminarBanner, name="eliminarBanner"),
    path('eliminarCat/<str:name>/', eliminarCategoria, name="eliminarCat"),
    path('eliminarPublico/<str:publico>/', eliminarPublico, name="eliminarPublico")


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
