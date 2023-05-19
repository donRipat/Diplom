from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import RouteForm


def routes(request):
    routes = Route.objects.all()
    form = RouteForm()
    dic = {
        'form': form,
        'routes': routes,
        'title': 'Населенные пункты',
    }
    return render(request, 'main/routes.html', dic)


def add(request):
    qd = request.POST
    st = City.objects.filter(id=qd.get('start_id'))[0]
    fin = City.objects.filter(id=qd.get('finish_id'))[0]
    Route.objects.create(
        start_city=st,
        finish_city=fin,
        price=qd.get('price'),
    )
    return HttpResponseRedirect("/routes")


def delete(request, id: int):
    Route.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/routes")
