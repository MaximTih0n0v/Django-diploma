from django.http import HttpResponse
from django.shortcuts import render
from apps.products.models import Categories


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Сервис аренды автомобилей',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Мы не передаём Ваши личные данные третьим лицам'

    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'Контактная информация',
        'content': 'Адрес: г.Минск пр.Победителей, 125',
        'text_on_page': 'Телефон: +375 (29) 789 96 69'

    }
    return render(request, 'main/contacts.html', context)


def delivery(request):
    context = {
        'title': 'Доставка и оплата',
        'content': 'Здесь может быть какая-то информация о доставке...',
        'text_on_page': ':)'

    }
    return render(request, 'main/delivery.html', context)
