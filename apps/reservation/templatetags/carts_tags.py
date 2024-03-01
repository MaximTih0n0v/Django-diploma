from django import template
from apps.reservation.models import Reservation

register = template.Library()


@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Reservation.objects.filter(user=request.user)
