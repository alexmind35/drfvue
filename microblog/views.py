from django.shortcuts import render


def index(request, path=''):
    """
    Главная страница. Контейнер для одностраничного плижения
    """
    return render(request, 'index.html')
