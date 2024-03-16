from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.contrib import messages

from apps.orders.forms import CreateOrderForm
from apps.orders.models import Order, OrderItem
from apps.reservation.models import Reservation


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Reservation.objects.filter(user=user)

                    if cart_items.exists():
                        # Создание заказа
                        order = Order.objects.create(
                            user=user,
                            phone=form.cleaned_data['phone'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                            hours=form.cleaned_data['hours'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < 1:
                                raise ValidationError(f'Недостаточное количество {name}\
                                                      В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                hours=form.cleaned_data['hours'],
                                created_at=cart_item.created_at,
                            )
                            product.quantity -= 1
                            product.save()

                        # Очистка корзины после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.warning(request, str(e))
                return redirect('users:profile')

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'patronymic': request.user.patronymic,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Оформление заказа',
        'form': form,
        'order': True,
    }

    return render(request, 'orders/create_order.html', context)
