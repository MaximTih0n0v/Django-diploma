from django.shortcuts import render, redirect
from apps.products.models import Products
from apps.reservation.models import Reservation
from django.http import JsonResponse
from django.template.loader import render_to_string

from apps.reservation.utils import get_user_carts


def reservation_add(request):

    product_id = request.POST.get('product_id')
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        reservation = Reservation.objects.filter(user=request.user, product=product)

        if reservation.exists():
            reservation = reservation.first()
            if reservation:
                reservation.quantity += 1
                reservation.save()
        else:
            Reservation.objects.create(user=request.user, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "includes/included_reservation.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def reservation_change(request, product_slug):
    ...


def reservation_remove(request, reservation_id):
    cart = Reservation.objects.get(id=reservation_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])
