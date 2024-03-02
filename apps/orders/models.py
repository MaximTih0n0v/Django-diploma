from django.db import models
from apps.users.models import User
from apps.products.models import Products


class OrderItemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.poducts_price for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')
    requires_delivery = models.BooleanField(default=False, verbose_name='Требуется доставка')
    delivery_address = models.TextField(blank=True, null=True, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=18, blank=True, null=True, verbose_name='Телефон')
    payment_on_get = models.BooleanField(default=False, verbose_name='Оплата при получении')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=50, default='В обработке', verbose_name='Статус заказа')
    hours = models.IntegerField(default=1, verbose_name='Часов аренды')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренда'

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name} | {self.user.phone}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name='Авто', default=None)
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    hours = models.IntegerField(default=10, verbose_name='Часов аренды')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'В аренде'
        verbose_name_plural = 'В аренде'

    objects = OrderItemQuerySet.as_manager()

    def save(self, *args, **kwargs):
        if self.order:
            self.hours = self.order.hours
        super(OrderItem, self).save(*args, **kwargs)

    def products_price(self):
        return round(self.price * self.hours, 2)

    def __str__(self):
        return f"Авто - {self.name} | Заказ № {self.order.pk}"



