from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement # импортируем таблицу (модель)
from .forms import AdvertisementForm
from django.urls import reverse

# Create your views here.(Создавайте свои представления здесь.)
def index(request): # Скрипт для главной страницы
    advertisements = Advertisement.objects.all() # вытаскиваем все данные (объявления) из модели
    context = {'advertisements':advertisements} # создаем словарь
    return render(request, 'index.html', context) # передаем в параметр созданную переменную

def top_sellers(request): # Скрипт для продавцов
    return render(request,'top-sellers.html')

def advertisement_post(request): # Скрипт для запонения формы от пользователя
    if request.method == "POST": # Если запрос = пост
        form = AdvertisementForm(request.POST, request.FILES) # То форма будет
        if form.is_valid(): # Если форма валидна
            advertisement = form.save(commit=False) # то форма такая
            advertisement.user = request.user # Добавим пользователя
            advertisement.save() # Сохраним форму
            url = reverse('main-page') # Достанем URL при помощи функции revers
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)