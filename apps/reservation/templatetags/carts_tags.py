from django import template
from apps.reservation.models import Reservation
from apps.reservation.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)
