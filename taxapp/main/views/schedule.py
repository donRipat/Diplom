from django.shortcuts import render
from ..models import *


def schedule(request):
    return render(request, 'main/schedule.html', {'title': 'Расписание'})
