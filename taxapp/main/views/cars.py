from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import CarForm


def cars(request):
    cars = Car.objects.all().order_by('-model')
    form = CarForm()
    dic = {
        'form': form,
        'cars': cars,
        'title': 'Автомобили',
    }
    return render(request, 'main/cars.html', dic)


def add(request):
    qd = request.POST
    Car.objects.create(
        model=qd.get('model'),
        plate=qd.get('plate'),
        sits=qd.get('sits')
    )
    return HttpResponseRedirect("/cars")


def delete(request, id: int):
    Car.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/cars")
