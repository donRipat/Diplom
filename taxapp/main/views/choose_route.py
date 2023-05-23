from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import *


def choose(request):
    schedule = ScheduledRoute.objects.all().order_by('route')
    form = RouteChoosingForm()
    dic = {
        'form': form,
        'schedule': schedule,
        'title': 'Расписание',
    }
    return render(request, 'main/choose_route.html', dic)


def route_edit(request):
    qd = request.POST
    print("'choose_route.py' Route.objects.filter(id=qd.get('route'))[0] = ",
          Route.objects.filter(id=qd.get('route'))[0])
    route = Route.objects.filter(id=qd.get('route'))[0]
    print("route.times.all() = ", route.times.all())
    times = route.times.all()
    form = TimeAddingForm()
    dic = {
        'form': form,
        'route': route,
        'times': times,
        'title': 'Добавить время для маршрута "' + str(route.start_area) +
                 ' — ' + str(route.finish_area) + '"',
    }
    return render(request, 'main/route_time.html', dic)

#
# def delete(request, id: int):
#     ScheduledRoute.objects.filter(id=id)[0].delete()
#     return HttpResponseRedirect("/schedule")
