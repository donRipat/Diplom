from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *
from ..forms import BookingForm


def bookings(request):
    form = BookingForm()
    dic = {
        'form': form,
        'title': 'Заказы',
    }
    return render(request, 'main/bookings.html', dic)


def add(request):
    qd = request.POST
    return HttpResponseRedirect("/bookings")


def delete(request, id: int):
    return HttpResponseRedirect("/bookings")
