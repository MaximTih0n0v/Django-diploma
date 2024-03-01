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

    else:
        carts = Reservation.objects.filter(
            session_key=request.session.session_key, product=product
        )
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Reservation.objects.create(
                session_key=request.session.session_key, product=product, quantity=1
            )
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "includes/included_reservation.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def reservation_change(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Reservation.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "includes/included_reservation.html", {"carts": cart}, request=request
    )
    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


def reservation_remove(request):

    cart_id = request.POST.get('cart_id')

    cart = Reservation.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "includes/included_reservation.html", {"carts": user_cart}, request=request
    )
    response_data = {
        "message": "Товар удалён",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)




