from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import CityForm


def cities(request):
    cities = City.objects.all().order_by('-name')
    form = CityForm()
    dic = {
        'form': form,
        'cities': cities,
        'title': 'Населенные пункты',
    }
    return render(request, 'main/cities.html', dic)


def add(request):
    qd = request.POST
    print(qd.get('area'))
    City.objects.create(
        name=qd.get('name'),
        area=Area.objects.filter(id=qd.get('area'))[0],
        est_time_ufa=qd.get('est_time_ufa'),
        dist_ufa=qd.get('dist_ufa'),
        price_addition=qd.get('price_addition')
    )
    return HttpResponseRedirect("/cities")


def delete(request, id: int):
    City.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/cities")
