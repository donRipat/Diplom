from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import *


def drives(request):
    drives = Drive.objects.all()
    drt = []
    for drive in drives:
        drt.append((drive, len(drive.passengers.all())))
    dic = {
        'drives': drives,
        'title': 'Поездки',
        'drt': drt,
    }
    return render(request, 'main/drives.html', dic)

