from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import ScheduleForm


def schedule(request):
    schedule = ScheduledRoute.objects.all().order_by('-route')
    form = ScheduleForm()
    dic = {
        'form': form,
        'schedule': schedule,
        'title': 'Расписание',
    }
    return render(request, 'main/schedule.html', dic)


def add(request):
    qd = request.POST
    print(qd.get('route'))
    ScheduledRoute.objects.create(
        route=Route.objects.filter(id=qd.get('route'))[0],
        time=qd.get('time')
    )
    return HttpResponseRedirect("/schedule")


def delete(request, id: int):
    ScheduledRoute.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/schedule")
