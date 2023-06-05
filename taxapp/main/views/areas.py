from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import AreaForm
from ..messages import get_info_message
from django.db import Error


def areas(request, mes):
    areas = Area.objects.all().order_by('name')
    form = AreaForm()
    dic = {
        'form': form,
        'areas': areas,
        'title': 'Локации маршрутов',
        'info_message': get_info_message(mes),
    }
    return render(request, 'main/areas.html', dic)


def add(request):
    try:
        qd = request.POST
        Area.objects.create(
            name=qd.get('name'),
        )
        return HttpResponseRedirect("/areas/1")
    except Error:
        return HttpResponseRedirect("/areas/101")


def delete(request, id: int):
    try:
        Area.objects.filter(id=id)[0].delete()
        return HttpResponseRedirect("/areas/2")
    except Error:
        return HttpResponseRedirect("/areas/102")
