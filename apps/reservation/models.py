from django.db import models
from apps.users.models import User
from apps.products.models import Products


class ReservationQuerySet(models.QuerySet):
    def total_price(self):
        return sum(reservation.products_price() for reservation in self)

    def total_quantity(self):
        if self:
            return sum(reservation.quantity for reservation in self)

        return 0


class Reservation(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Авто')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')
    start_datetime = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время начала бронирования')
    end_datetime = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время окончания бронирования')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    class Meta:
        db_table = 'reservation'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    objects = ReservationQuerySet().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return (f'Корзина {self.user.username} | Автомобиль {self.product.name} | Количество {self.quantity} | '
                f'Начало бронирования {self.start_datetime}| Окончание бронирования {self.end_datetime}')
