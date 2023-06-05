from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import *
from ..arrangement.new_booking import new_booking_handle
from ..messages import get_info_message
from django.db import Error
from django.core.exceptions import ValidationError


def choose(request):
    schedule = ScheduledRoute.objects.all()
    tt = []
    routes = Route.objects.all().order_by('start_area')
    for r in routes:
        times = []
        for time in r.times.all().order_by('time'):
            times.append(time.time)
        tt.append((f"{r.start_area} — {r.finish_area}", times, r.id))

    form = RouteChoosingForm()
    dic = {
        'form': form,
        'schedule': schedule,
        'title': 'Расписание',
        'tt': tt,
    }
    return render(request, 'main/choose_route.html', dic)


def route_edit(request, id: int, mes):
    qd = request.POST
    route = Route.objects.filter(id=id)[0]
    times = route.times.all().order_by('time')
    form = TimeAddingForm()
    dic = {
        'form': form,
        'route': route,
        'times': times,
        'title': 'Добавить время для маршрута "' + str(route.start_area) +
                 ' — ' + str(route.finish_area) + '"',
        'info_message': get_info_message(mes),
    }
    return render(request, 'main/route_time.html', dic)


def add(request, id):
    qd = request.POST
    route = Route.objects.filter(id=id)[0]
    try:
        ScheduledRoute.objects.create(
            route=route,
            time=qd.get('time'),
        )
        return HttpResponseRedirect(f"/route/{id}/1")
    except Error:
        return HttpResponseRedirect(f"/route/{id}/101")
    except ValidationError:
        return HttpResponseRedirect(f"/route/{id}/103")


def delete(request, r_id: int, t_id: int):
    try:
        ScheduledRoute.objects.filter(id=t_id)[0].delete()
        return HttpResponseRedirect(f"/route/{r_id}/2")
    except:
        return HttpResponseRedirect(f"/route/{r_id}/102")
