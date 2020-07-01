from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import UsuarioForm, Hero, Banner, Aside, Clothes, Publico, Cat, Publico
from .models import HeroSeccion, BannerSection, AsideImage, Clothing, Persona, Category, Persona
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.db.models import Count, F
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect, Http404
from aplicaciones.favorites.models import Favorito
import json 

# Create your views here.
def autenticacion(request):
    if not request.user.is_superuser:
        raise PermissionDenied()

def paginaInicio(request):
    images = HeroSeccion.objects.all()
    banners = BannerSection.objects.all()
    aside = AsideImage.objects.filter(publico = "Mujeres")
    asideHom = AsideImage.objects.filter(publico = "Hombres")
    clothe = Clothing.objects.filter(cat="Ropa", publico="Mujeres")
    clotheCart = Clothing.objects.filter(cat="Carteras", publico="Mujeres")
    clotheZap = Clothing.objects.filter(cat="Zapatos", publico="Mujeres")
    clotheAcc = Clothing.objects.filter(cat="Accesorios", publico="Mujeres")
    clotheH = Clothing.objects.filter(cat="Ropa", publico="Hombres")
    clotheCartH = Clothing.objects.filter(cat="Carteras", publico="Hombres")
    clotheZapH = Clothing.objects.filter(cat="Zapatos", publico="Hombres")
    clotheAccH = Clothing.objects.filter(cat="Accesorios", publico="Hombres")
    contexto={
        'images':images,
        'banner':banner,
        'banners': banners,
        'aside':aside,
        'clothe': clothe,
        'asideHom':asideHom,
        'clotheCart':clotheCart,
        'clotheZap':clotheZap,
        'clotheAcc':clotheAcc,
        'clotheH': clotheH,
        'clotheCartH':clotheCartH,
        'clotheZapH':clotheZapH,
        'clotheAccH':clotheAccH,
        }
    if request.user.is_superuser:
        return redirect('principal:own')
    else:
        if request.user.is_authenticated:
            return render(request, 'indexcostumer.html', contexto )
        else:
            return render(request, 'inicio.html', contexto )
    
    return render(request, 'inicio.html', contexto )

def inicioCostumer(request):
    favorites= Favorito.objects.filter(user=request.user)
    cantFav= len(Favorito.objects.filter(user=request.user))
    images = HeroSeccion.objects.all()
    banners = BannerSection.objects.all()
    aside = AsideImage.objects.filter(publico = "Mujeres")
    asideHom = AsideImage.objects.filter(publico = "Hombres")
    clothe = Clothing.objects.filter(cat="Ropa", publico="Mujeres")
    clotheCart = Clothing.objects.filter(cat="Carteras", publico="Mujeres")
    clotheZap = Clothing.objects.filter(cat="Zapatos", publico="Mujeres")
    clotheAcc = Clothing.objects.filter(cat="Accesorios", publico="Mujeres")
    clotheH = Clothing.objects.filter(cat="Ropa", publico="Hombres")
    clotheCartH = Clothing.objects.filter(cat="Carteras", publico="Hombres")
    clotheZapH = Clothing.objects.filter(cat="Zapatos", publico="Hombres")
    clotheAccH = Clothing.objects.filter(cat="Accesorios", publico="Hombres")
    contexto={
        'images':images,
        'banner':banner,
        'banners': banners,
        'aside':aside,
        'clothe': clothe,
        'asideHom':asideHom,
        'clotheCart':clotheCart,
        'clotheZap':clotheZap,
        'clotheAcc':clotheAcc,
        'clotheH': clotheH,
        'clotheCartH':clotheCartH,
        'clotheZapH':clotheZapH,
        'clotheAccH':clotheAccH,
        'favorites': favorites,
        'cantFav': cantFav
        }
    return render(request, 'indexcostumer.html', contexto )
def producto(request,id):
    prod= Clothing.objects.filter(id = id)
    contexto ={
        'prod':prod
    }
    return render(request, 'product.html', contexto)

def shopM(request):
    todos= Clothing.objects.filter(publico = "Mujeres")
    contexto={
        'todos':todos
    }
    return render(request, 'shop.html', contexto)

def shopH(request):
    todos= Clothing.objects.filter(publico = "Hombres")
    contexto={
        'todos':todos
    }
    return render(request, 'shop.html', contexto)

#Las siguientes funciones necesitan permisos de superuser

def inicioOwner(request):

    if request.method =="GET":
        favorites= Favorito.objects.filter(user=request.user)
        cantFav= len(Favorito.objects.filter(user=request.user))
        images = HeroSeccion.objects.all()
        banners = BannerSection.objects.all()
        aside = AsideImage.objects.filter(publico = "Mujeres")
        asideHom = AsideImage.objects.filter(publico = "Hombres")
        public= Persona.objects.all()
        publico = Publico()
        likes = Clothing()
        clothe = Clothing.objects.filter(cat="Ropa", publico="Mujeres")
        clotheCart = Clothing.objects.filter(cat="Carteras", publico="Mujeres")
        clotheZap = Clothing.objects.filter(cat="Zapatos", publico="Mujeres")
        clotheAcc = Clothing.objects.filter(cat="Accesorios", publico="Mujeres")
        clotheH = Clothing.objects.filter(cat="Ropa", publico="Hombres")
        clotheCartH = Clothing.objects.filter(cat="Carteras", publico="Hombres")
        clotheZapH = Clothing.objects.filter(cat="Zapatos", publico="Hombres")
        clotheAccH = Clothing.objects.filter(cat="Accesorios", publico="Hombres")
        categories= Cat()
        category= Category.objects.all()
        asideForm =Aside()
        banner = Banner()
        cat = Clothes()
        form = Hero()
        contexto={
            'images':images,
            'form':form,
            'banner':banner,
            'banners': banners,
            'aside':aside,
            'asideForm': asideForm,
            'cat': cat,
            'clothe': clothe,
            'categories': categories,
            'category':category,
            'publico': publico,
            'public':public,
            'asideHom':asideHom,
            'clotheCart':clotheCart,
            'clotheZap':clotheZap,
            'clotheAcc':clotheAcc,
            'clotheH': clotheH,
            'clotheCartH':clotheCartH,
            'clotheZapH':clotheZapH,
            'clotheAccH':clotheAccH,
            'likes':likes,
            'favorites': favorites,
            'cantFav': cantFav
            }
            
    if request.method == "POST": 
        form = Hero(request.POST or None, request.FILES or None)
        banner= Banner(request.POST or None, request.FILES or None)
        aside = Aside(request.POST or None, request.FILES or None)
        cat = Clothes(request.POST or None, request.FILES or None)
        cate = Cat(request.POST)
        publico= Publico(request.POST)
        contexto ={
            'form':form,
            'banner':banner,
            'aside': aside,
            'cat': cat,
            'cate': cate,
            'publico':publico
        }
        if publico.is_valid():
            publico.save()
            return redirect('principal:own')
        if aside.is_valid():
            aside.save()
            return redirect('principal:own')
        if cate.is_valid():
            cate.save()
            return redirect('principal:own')
        if cat.is_valid():
            cat.save()
            return redirect('principal:own') 
        if form.is_valid():
            form.save()
            return redirect('principal:own')
        if banner.is_valid():
            banner.save()
            return redirect('principal:own')   
    return render(request, 'index.html', contexto )



def banner(request):
    autenticacion()
    if request.method=="GET":
        form= Banner()
        contexto={
            'form':form
        }
    if request.method == "POST":
        form=Banner(request.POST or None, request.FILES or None)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('principal:index')
    return render(request, 'banner.html', contexto )


def login(request):
    if request.user.is_superuser:
        return redirect('principal:own')
    if request.user.is_authenticated:
        return redirect('principal:inicio')
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                if user.is_staff:
                    do_login(request, user)
                # Y le redireccionamos a la portada
                    return redirect('principal:own')
                else:
                    do_login(request, user)
                    return redirect('principal:inicio')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'login.html',{'form': form} )

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('principal:index')
    
def register(request):
    if request.method == 'GET':
    # Creamos el formulario de autenticación vacío
        form = UsuarioForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UsuarioForm(data=request.POST)
        # Si el formulario es válido...
        
        if form.is_valid():
                
            # Creamos la nueva cuenta de usuario
            user = form.save()

            # # Si el usuario se crea correctamente 
            return redirect('principal:index')
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
   

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})

def cambios(request,id):
    autenticacion()
    img= HeroSeccion.objects.get(id = id)
    if request.method == 'GET':
        form = Hero(instance = img)
        contexto = {
            'form':form
        }
    else:
        form= Hero(request.POST, instance = img)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('principal:index')
    return render(request,'changehero.html',contexto)

def cambiosAside(request,id):
    autenticacion()
    aside= AsideImage.objects.get(id = id)
    if request.method == 'GET':
        form = Aside(instance = aside)
        contexto = {
            'form':form
        }
    else:
        form= Aside(request.POST, instance = aside)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('principal:index')
    return render(request,'aside.html',contexto)

def cambiosbanner(request,id):
    autenticacion()
    ban=BannerSection.objects.get(id = id)
    if request.method == "GET":
        form = Banner(instance = ban)
        contexto = {
            'form': form
        }
    else:
        form = Banner(request.POST, instance = ban)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('principal:index')
    autenticacion(request)
    return render(request,'banner.html',contexto)


def eliminarPromo(request,id):
    autenticacion()
    img= HeroSeccion.objects.get(id=id)
    img.delete()
    return redirect('principal:index')

def eliminarBanner(request,id):
    autenticacion()
    ban= BannerSection.objects.get(id = id)
    ban.delete()
    return redirect('principal:index')

def eliminarCategoria(request,name):
    autenticacion()
    cat= Category.objects.get(name=name)
    cat.delete()
    return redirect('principal:index')

def eliminarPublico(request, publico):
    autenticacion()
    pub= Persona.objects.get(publico = publico)
    pub.delete()
    return redirect('principal:index')


