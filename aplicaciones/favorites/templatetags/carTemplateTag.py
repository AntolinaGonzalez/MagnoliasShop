from django import template
from aplicaciones.principal.models import Order, OrderItem


register = template.Library()

@register.filter
def cartItem(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

