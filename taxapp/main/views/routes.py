from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import RouteForm
from ..messages import get_info_message
from django.db import Error


def routes(request, mes):
    routes = Route.objects.all()
    form = RouteForm()
    dic = {
        'form': form,
        'routes': routes,
        'title': 'Маршруты',
        'info_message': get_info_message(mes),
    }
    return render(request, 'main/routes.html', dic)


def add(request):
    try:
        qd = request.POST
        print("routes.py qd.get('no_reverse_route') = ", qd.get('no_reverse_route'))
        print('routes.py start_area = ', qd.get('start_area'))
        if qd.get('start_area') == qd.get('finish_area'):
            return HttpResponseRedirect("/routes/101")
        st = Area.objects.filter(id=qd.get('start_area'))[0]
        fin = Area.objects.filter(id=qd.get('finish_area'))[0]
        Route.objects.create(
            start_area=st,
            finish_area=fin,
            price=qd.get('price'),
        )
        if qd.get('no_reverse_route'):
            return HttpResponseRedirect("/routes/1")
        Route.objects.create(
            start_area=fin,
            finish_area=st,
            price=qd.get('price'),
        )
        return HttpResponseRedirect("/routes/1")
    except Error:
        return HttpResponseRedirect("/routes/101")


def delete(request, id: int):
    try:
        Route.objects.filter(id=id)[0].delete()
        return HttpResponseRedirect("/routes/2")
    except Error:
        return HttpResponseRedirect("/routes/102")
