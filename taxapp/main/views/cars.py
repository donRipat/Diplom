from django.shortcuts import render
from ..models import *


def cars(request):
    cars = Car.objects.all()
    return render(request, 'main/cars.html', {'title': 'Автомобили', 'cars': cars})
