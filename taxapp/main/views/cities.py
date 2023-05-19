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
    City.objects.create(
        name=qd.get('name'),
        parent_city_id=qd.get('parent_city_id'),
        est_time_ufa=qd.get('est_time_ufa'),
        est_time_addition=qd.get('est_time_addition'),
        dist_ufa=qd.get('dist_ufa'),
        dist_parent=qd.get('dist_parent'),
        price_addition=qd.get('price_addition')
    )
    return HttpResponseRedirect("/cities")


def delete(request, id: int):
    City.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/cities")
