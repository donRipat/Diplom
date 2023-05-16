from django.shortcuts import render
from ..models import *


def employees(request):
    drivers = Driver.objects.all()
    return render(request, 'main/employees.html', {'title': 'Водители', 'employees': drivers})
