from apps.reservation.models import Reservation


def get_user_carts(request):
    if request.user.is_authenticated:
        return Reservation.objects.filter(user=request.user)

    if not request.session.session_key:
        request.session.create()
    return Reservation.objects.filter(session_key=request.session.session_key)
