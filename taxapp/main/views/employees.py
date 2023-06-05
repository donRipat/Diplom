from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import DriverForm
from ..messages import get_info_message
from django.db import Error


def employees(request, mes):
    m = Driver.objects.all().order_by('-name')
    form = DriverForm()
    dic = {
        'form': form,
        'drivers': m,
        'title': 'Водители',
        'info_message': get_info_message(mes),
    }
    return render(request, 'main/employees.html', dic)


def add(request):
    try:
        qd = request.POST
        Driver.objects.create(
            name=qd.get('name'),
            phone=qd.get('phone')
        )
        return HttpResponseRedirect("/employees/1")
    except Error:
        return HttpResponseRedirect("/employees/101")


def delete(request, id: int):
    try:
        Driver.objects.filter(id=id)[0].delete()
        return HttpResponseRedirect("/employees/2")
    except Error:
        return HttpResponseRedirect("/employees/102")
