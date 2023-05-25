from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import *


def drive_details(request, id: int):
    passengers = Drive.objects.filter(id=id)[0].passengers.all()
    stops = []
    for p in passengers:
        stops.append(
            (
                p.booking.start_city.dist_ufa,
                p.booking.start_city.name,
                p.booking.start_address,
            )
        )
        stops.append(
            (
                p.booking.finish_city.dist_ufa,
                p.booking.finish_city.name,
                p.booking.finish_address,
            )
        )

    dic = {
        'passengers': passengers,
        'title': 'Детали поездки',
        'stops': sorted(stops),
    }
    return render(request, 'main/drive_details.html', dic)
