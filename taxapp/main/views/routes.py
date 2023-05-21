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
    print(qd.get('start_area'))
    st = Area.objects.filter(id=qd.get('start_area'))[0]
    fin = Area.objects.filter(id=qd.get('finish_area'))[0]
    Route.objects.create(
        start_area=st,
        finish_area=fin,
        price=qd.get('price'),
    )
    return HttpResponseRedirect("/routes")


def delete(request, id: int):
    Route.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/routes")
