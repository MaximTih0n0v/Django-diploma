from django.urls import path

from apps.reservation import views

app_name = 'reservation'

urlpatterns = [
    path('reservation_add/<int:product_id>/', views.reservation_add, name='reservation_add'),
    path('reservation_change/<int:product_id>/', views.reservation_change, name='reservation_change'),
    path('reservation_remove/<int:product_id>/', views.reservation_remove, name='reservation_remove'),
]
