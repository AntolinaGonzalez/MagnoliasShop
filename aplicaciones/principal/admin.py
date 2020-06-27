from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(BannerSection)
admin.site.register(AsideImage)
admin.site.register(HeroSeccion)
admin.site.register(Clothing)
admin.site.register(Category)
admin.site.register(Persona)


