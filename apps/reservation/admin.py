from django.contrib import admin
from apps.reservation.models import Reservation


class ReservationTabAdmin(admin.TabularInline):
    model = Reservation
    fields = ['product', 'quantity', 'created_at']
    search_fields = ['product', 'quantity', 'created_at']
    readonly_fields = ['created_at']
    extra = 1


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'created_at']
    list_filter = ['created_at', 'user', 'product']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"




