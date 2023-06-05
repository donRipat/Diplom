from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import CityForm
from ..messages import get_info_message
from django.db import Error
from django.core.exceptions import ValidationError


def cities(request, mes):
    cities = City.objects.all().order_by('-name')
    form = CityForm()
    dic = {
        'form': form,
        'cities': cities,
        'title': 'Населенные пункты',
        'info_message': get_info_message(mes),
    }
    return render(request, 'main/cities.html', dic)


def add(request):
    try:
        qd = request.POST
        print("--cities.py--\nqd.get('area') = ", qd.get('area'))
        City.objects.create(
            name=qd.get('name'),
            area=Area.objects.filter(id=qd.get('area'))[0],
            est_time_ufa=qd.get('est_time_ufa'),
            dist_ufa=qd.get('dist_ufa'),
            price_addition=qd.get('price_addition')
        )
        return HttpResponseRedirect("/cities/1")
    except Error:
        return HttpResponseRedirect("/cities/101")
    except ValidationError:
        return HttpResponseRedirect("/cities/103")


def delete(request, id: int):
    try:
        City.objects.filter(id=id)[0].delete()
        return HttpResponseRedirect("/cities/2")
    except Error:
        return HttpResponseRedirect("/cities/102")
