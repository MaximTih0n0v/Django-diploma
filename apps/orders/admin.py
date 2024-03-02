from django.contrib import admin

from apps.orders.models import Order, OrderItem


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'name', 'price')
    search_fields = ('product', 'name')
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'name', 'price')
    search_fields = ('order', 'product', 'name')


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = ('requires_delivery', 'status', 'payment_on_get', 'is_paid', 'created_at')

    search_fields = ('requires_delivery', 'status', 'payment_on_get', 'is_paid', 'created_at')
    readonly_fields = ('created_at',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'hours',
        'created_at'
    )
    search_fields = (
        'id',
    )
    readonly_fields = ('created_at',)
    list_filter = (
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
    )
    inlines = (OrderItemTabularAdmin,)