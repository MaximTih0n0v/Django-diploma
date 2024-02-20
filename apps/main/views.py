from django.http import HttpResponse
from django.shortcuts import render


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
