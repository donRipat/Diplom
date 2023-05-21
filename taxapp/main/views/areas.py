from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import AreaForm


def areas(request):
    areas = Area.objects.all().order_by('-name')
    form = AreaForm()
    dic = {
        'form': form,
        'areas': areas,
        'title': 'Локации маршрутов',
    }
    return render(request, 'main/areas.html', dic)


def add(request):
    qd = request.POST
    Area.objects.create(
        name=qd.get('name'),
    )
    return HttpResponseRedirect("/areas")


def delete(request, id: int):
    Area.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/areas")
