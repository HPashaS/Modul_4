from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement # импортируем таблицу (модель)

# Create your views here.(Создавайте свои представления здесь.)
def index(request):
    advertisements = Advertisement.objects.all() # вытаскиваем все данные (объявления) из модели
    context = {'advertisements':advertisements} # создаем словарь
    return render(request, 'index.html', context) # передаем в параметр созданную переменную

def top_sellers(request):
    return render(request,'top-sellers.html')