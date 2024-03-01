from django.contrib import admin

from apps.reservation.admin import ReservationTabAdmin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'phone']
    search_fields = ['last_name', 'first_name', 'email', 'phone']

    inlines = [ReservationTabAdmin]
