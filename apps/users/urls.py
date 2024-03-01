from django.urls import path

from apps.users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-reservation/', views.users_reservation, name='users_reservation'),
    path('logout/', views.logout, name='logout'),
]
