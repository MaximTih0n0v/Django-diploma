from django.urls import path

from apps.reservation import views

app_name = 'reservation'

urlpatterns = [
    path('reservation_add/', views.reservation_add, name='reservation_add'),
    path('reservation_change/', views.reservation_change, name='reservation_change'),
    path('reservation_remove/', views.reservation_remove, name='reservation_remove'),
]
