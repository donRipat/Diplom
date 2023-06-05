from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import CarForm
from ..messages import get_info_message
from django.db import Error
from django.core.exceptions import ValidationError


def cars(request, mes):
    cars = Car.objects.all().order_by('-model')
    form = CarForm()
    dic = {
        'form': form,
        'cars': cars,
        'title': 'Автомобили',
        'info_message': get_info_message(mes),
    }
    return render(request, 'main/cars.html', dic)


def add(request):
    try:
        qd = request.POST
        Car.objects.create(
            model=qd.get('model'),
            plate=qd.get('plate'),
            sits=qd.get('sits')
        )
        return HttpResponseRedirect("/cars/1")
    except Error:
        return HttpResponseRedirect("/cars/101")


def delete(request, id: int):
    try:
        Car.objects.filter(id=id)[0].delete()
        return HttpResponseRedirect("/cars/2")
    except Error:
        return HttpResponseRedirect("/cars/102")
