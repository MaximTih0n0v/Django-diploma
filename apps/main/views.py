from django.http import HttpResponse
from django.shortcuts import render
from apps.products.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home - Главная',
        'content': 'Сервис аренды автомобилей',
        'categories': categories

    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Мы не передаём Ваши личные данные третьим лицам'

    }
    return render(request, 'main/about.html', context)
