from django.urls import path
from .views import inicio,login, register, logout, cambios, eliminarPromo, cambios, cambiosbanner, eliminarBanner
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
    path('eliminarBanner/<int:id>/', eliminarBanner, name="eliminarBanner")

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
