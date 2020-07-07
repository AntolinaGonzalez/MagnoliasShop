from django import template
from aplicaciones.favorites.models import Favorito


register = template.Library()

@register.filter
def favoritos(user):
    if user.is_authenticated:
        fav = Favorito.objects.filter(user=user)
        if fav.exists():
            return fav.count()
    return 0