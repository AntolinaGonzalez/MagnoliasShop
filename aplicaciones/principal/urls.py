from django.urls import path
from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from aplicaciones.favorites import views
from aplicaciones.favorites.views import marcador

urlpatterns = [
    path('', paginaInicio, name="index"),
    path('own/', inicioOwner, name="own"),
    path('inicio', inicioCostumer, name="inicio"),
    path('login/', login, name="login"),
    path('register/',register, name="register"),
    path('salir/', logout, name="salir"),
    path('cambios/<int:id>/', cambios, name="cambios"),
    path('eliminarPromo/<int:id>/', eliminarPromo, name="eliminar"),
    path('cambiosbanner/<int:id>/', cambiosbanner, name="banner"),
    path('cambiosAside/<int:id>/', cambiosAside, name="cambiosAside"),
    path('eliminarBanner/<int:id>/', eliminarBanner, name="eliminarBanner"),
    path('eliminarCat/<str:name>/', eliminarCategoria, name="eliminarCat"),
    path('eliminarPublico/<str:publico>/', eliminarPublico, name="eliminarPublico"),
    path('producto/<pk>/', ProductView.as_view(), name="producto"),
    path('shop/', HomeView.as_view(), name="shop"),
    path('shopH/', HomeViewMan.as_view(), name="shopH"),
    url(r'^marcar/favorito/(?P<pk>\d+)/marcador/$', marcador, name="marcar"),
    path('addToCart/<pk>/', addToCart, name="addToCart"),
    path('OrderSummary/', OrderSummary.as_view(), name="OrderSummary"),
    path('removeFromCart/<pk>/', removeFromCart, name="removeFromCart"),
    path('removeItem/<pk>/', removeItemFromCart, name="removeItem")

    

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
