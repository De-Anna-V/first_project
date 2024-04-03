from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now() 
    if current_time.hour in [2, 3, 4, 22, 23, 24]:
        msg = f'Текущее время: {current_time.hour} часа {current_time.minute} минут'
    elif current_time.hour in [1, 21]:
        msg = f'Текущее время: {current_time.hour} час {current_time.minute} минут'
    else:
        msg = f'Текущее время: {current_time.hour} часов {current_time.minute} минут'
    return HttpResponse(msg)


def workdir_view(request):
    list_d = []
    for filename in os.listdir('C:/Users/Анна/Desktop/f_project'):
        list_d.append(filename)
    return HttpResponse(', '.join(list_d))

