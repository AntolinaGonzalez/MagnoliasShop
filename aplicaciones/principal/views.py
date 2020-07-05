from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.conf import settings
from .forms import UsuarioForm, Hero, Banner, Aside, Clothes, Publico, Cat, Publico, CheckOutForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib import messages
from django.db.models import Count, F
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from aplicaciones.favorites.models import Favorito
from django.views.generic import ListView, DetailView, View
import json 
import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


# Create your views here.
def autenticacion(request):
    if not request.user.is_superuser:
        raise PermissionDenied()
def loginReq(request):
    if not request.user.is_authenticated:
        return redirect('principal:login')

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

class checkoutView(View):
    def get(self, *args, **kwargs):
        form= CheckOutForm
        contexto = {
            'form':form
        }
        return render(self.request, 'check-out.html', contexto)

    def post(self, *args, **kwargs):
        form= CheckOutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                direccion = form.cleaned_data.get('direccion')
                firstname = form.cleaned_data.get('firstname')
                lastname = form.cleaned_data.get('lastname')
                country = form.cleaned_data.get('country')
                codigo_postal = form.cleaned_data.get('codigo_postal')
                #same_billing_adress = form.cleaned_data.get('same_billing_adress')
                #save_info = form.cleaned_data.get('save_info')
                opcionesdepago = form.cleaned_data.get('opcionesdepago')
                billingAdress = BillingAdress(
                    user=self.request.user,
                    country=country,
                    #direccion y cd no anda lpm
                )
                billingAdress.save()
                order.billing_address = billingAdress
                order.save()
                if opcionesdepago == 'S':
                    return redirect('principal:Payment', payment_options='stripe')
                elif opcionesdepago == 'P': 
                    return redirect('principal:Payment', payment_options='paypal')
                else:
                    messages.warning(self.request, 'Invalid payment option')
                    return redirect('principal:checkout') 
            
            return redirect('principal:checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, 'Error')
        
class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'payment.html')
    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount= int(order.getTotalPrice() * 100)
        try:
  # Use Stripe's library to make requests...
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source = "tok_amex"
            )
            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = self.request.user
            payment.amount = order.getTotalPrice()
            payment.save()

            order.ordered = True
            order.payment = payment
            order.save()

            messages.success(self.request, "Your order was succesful")
            return redirect('/')
        except stripe.error.CardError as e:
  # Since it's a decline, stripe.error.CardError will be caught
            body=e.json.body
            err = body.get('error', {})
            messages.error(self.request, f"{err.get('message')}")
            return redirect('/')
        except stripe.error.RateLimitError as e:
  # Too many requests made to the API too quickly
            messages.error(self.request, "Rate limit error")
            
        except stripe.error.InvalidRequestError as e:
  # Invalid parameters were supplied to Stripe's API
            print('Status is: %s' % e.http_status)
            print('Type is: %s' % e.error.type)
            print('Code is: %s' % e.error.code)
            # param is '' in this case
            print('Param is: %s' % e.error.param)
            print('Message is: %s' % e.error.message)
            messages.error(self.request, 'Message is: %s' % e.error.message)
            return redirect('/')
            
        except stripe.error.AuthenticationError as e:
  # Authentication with Stripe's API failed
  # (maybe you changed API keys recently)
            messages.error(self.request, "Not aunthenticated")
            return redirect('/')
        except stripe.error.APIConnectionError as e:
  # Network communication with Stripe failed
            messages.error(self.request, "API ERROR")
            return redirect('/')
        except stripe.error.StripeError as e:
  # Display a very generic error to the user, and maybe send
  # yourself an email
            messages.error(self.request, "STRIPE ERROR")
            return redirect('/')
        except Exception as e:
  # Something else happened, completely unrelated to Stripe
            messages.error(self.request, "EXCEPTION")
            return redirect('/')
        
class HomeView(ListView):
    queryset= Clothing.objects.filter(publico = "Mujeres")
    paginate_by=6
    template_name = 'shop.html'

class HomeViewMan(ListView):
    queryset= Clothing.objects.filter(publico = "Hombres")
    paginate_by=6
    template_name = 'shop.html'
    
class ProductView(DetailView):
    model = Clothing
    template_name = 'product.html'

class OrderSummary(View):
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            try:
                order = Order.objects.get(user=self.request.user, ordered=False)
                contexto ={
                    'order': order
                }
                return render(self.request, 'shopping-cart.html', contexto)
            except ObjectDoesNotExist:
                messages.error(self.request, 'Error')
                return redirect('principal:HomeView')
        else:
            return redirect('principal:login')

        


def addToCart(request,pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Clothing, pk=pk)
        order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
        order_qs= Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists() :
            order= order_qs[0]

            if order.items.filter(item__id=item.id).exists():
                order_item.quantity += 1
                order_item.save()
                messages.info(request, 'Your item was updated')
                return redirect('principal:OrderSummary')
            else:
                messages.info(request, 'Your item was added')
                order.items.add(order_item)
        else:
            order= Order.objects.create(user=request.user)
            order.items.add(order_item)
    else:
        return redirect('principal:login')
    return redirect('principal:producto', pk=pk)

def removeFromCart(request,pk):
    item = get_object_or_404(Clothing, pk=pk)
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists() :
        order= order_qs[0]

        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, 'Your item was removed')
            return redirect('principal:OrderSummary')
        else:
            messages.info(request, 'This item was not in your cart')
            return redirect('principal:producto', pk=pk)
    else:
        messages.info(request, 'You do not have an active order')
        return redirect('principal:producto', pk=pk)
    return redirect('principal:producto', pk=pk)

def removeItemFromCart(request,pk):
    item = get_object_or_404(Clothing, pk=pk)
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists() :
        order= order_qs[0]

        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else: 
                order.items.remove(order_item)
            
            return redirect('principal:OrderSummary')
        else:
            messages.info(request, 'This item was not in your cart')
            return redirect('principal:producto', pk=pk)
    else:
        messages.info(request, 'You do not have an active order')
        return redirect('principal:producto', pk=pk)
    return redirect('principal:producto', pk=pk)
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


