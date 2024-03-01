from apps.reservation.models import Reservation


def get_user_carts(request):
    if request.user.is_authenticated:
        return Reservation.objects.filter(user=request.user)
