from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import DriverForm


def employees(request):
    m = Driver.objects.all().order_by('-name')
    form = DriverForm()
    dic = {
        'form': form,
        'drivers': m,
        'title': 'Водители',
    }
    return render(request, 'main/employees.html', dic)


def add(request):
    qd = request.POST
    Driver.objects.create(
        name=qd.get('name'),
        phone=qd.get('phone')
    )
    return HttpResponseRedirect("/employees")


def delete(request, id: int):
    Driver.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/employees")
