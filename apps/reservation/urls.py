from django.urls import path

from apps.reservation import views

app_name = 'reservation'

urlpatterns = [
    path('reservation_add/<slug:product_slug>/', views.reservation_add, name='reservation_add'),
    path('reservation_change/<slug:product_slug>/', views.reservation_change, name='reservation_change'),
    path('reservation_remove/<slug:product_slug>/', views.reservation_remove, name='reservation_remove'),
]
