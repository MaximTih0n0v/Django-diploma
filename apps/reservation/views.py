from django.shortcuts import render, redirect
from apps.products.models import Products
from apps.reservation.models import Reservation


def reservation_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        reservation = Reservation.objects.filter(user=request.user, product=product)

        if reservation.exists():
            reservation = reservation.first()
            if reservation:
                reservation.quantity += 1
                reservation.save()
        else:
            Reservation.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def reservation_change(request, product_slug):
    ...


def reservation_remove(request, reservation_id):
    cart = Reservation.objects.get(id=reservation_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])
