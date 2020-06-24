from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UsuarioForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class Hero(forms.ModelForm):
    class Meta:
        model = HeroSection
        fields = "__all__"

class Banner(forms.ModelForm):
    class Meta:
        model = BannerSection
        fields = "__all__"


class Aside(forms.ModelForm):
    class Meta:
        model = AsideImage
        fields = "__all__"

class Clothes(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = "__all__"