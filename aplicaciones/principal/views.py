from django.shortcuts import render, redirect
from django import forms
from .forms import UsuarioForm, Hero, Banner
from .models import HeroSection, BannerSection, AsideImage
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout
# Create your views here.


def inicio(request):
    if request.method=="GET":
        images = HeroSection.objects.all()
        banners = BannerSection.objects.all()
        aside= AsideImage.objects.all()
        banner = Banner()
        form = Hero()
        contexto={
            'images':images,
            'form':form,
            'banner':banner,
            'banners': banners,
            'aside':aside
         }
    if request.method == "POST": 
        form = Hero(request.POST or None, request.FILES or None)
        banner= Banner(request.POST or None, request.FILES or None)
        contexto ={
            'form':form,
            'banner':banner
        } 
        if form.is_valid():
            form.save()
            img_obj = form.instance 
            return redirect('principal:index')
        if banner.is_valid():
            banner.save()
            return redirect('principal:index')
    return render(request, 'index.html', contexto )

def banner(request):
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
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('principal:index')

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
    img= HeroSection.objects.get(id = id)
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

def cambiosbanner(request,id):
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
    return render(request,'banner.html',contexto)


def eliminarPromo(request,id):
    img= HeroSection.objects.get(id=id)
    img.delete()
    return redirect('principal:index')

def eliminarBanner(request,id):
    ban= BannerSection.objects.get(id = id)
    ban.delete()
    return redirect('principal:index')
