from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import BookingForm
from ..arrangement.new_booking import new_booking_handle


def bookings(request):
    form = BookingForm()
    bookings = Booking.objects.all()
    dic = {
        'form': form,
        'title': 'Заказы',
        'bookings': bookings,
    }
    return render(request, 'main/bookings.html', dic)


def add(request):
    qd = request.POST
    ds = qd.get('date')
    ds = ds[6:] + '-' + ds[3:5] + '-' + ds[0:2]
    b = Booking.objects.create(
        client_name=qd.get('client_name'),
        client_phone=qd.get('client_phone'),
        start_city=City.objects.filter(id=qd.get('start_city'))[0],
        finish_city=City.objects.filter(id=qd.get('finish_city'))[0],
        scheduled_route=ScheduledRoute.objects.filter(id=qd.get('scheduled_route'))[0],
        date=ds,
        start_address=qd.get('start_address'),
        finish_address=qd.get('finish_address'),
    )
    new_booking_handle(b)
    return HttpResponseRedirect("/bookings")


def delete(request, id: int):
    Booking.objects.filter(id=id)[0].delete()
    return HttpResponseRedirect("/bookings")
